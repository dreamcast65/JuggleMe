# JuggleMe

## Link to download Vulnerable server
https://drive.google.com/file/d/1D79WJ7gtECDag9_kxquUoUGX4fDHaJ-t/view?usp=sharing

If you do not have VMware Fusion or VMware Workstation the application is available at http://da45-107-181-178-100.ngrok.io/Login.php.  You will need to install ngrok to receive your reverse shell and will have to either modify the script or set up ngrok with a netcat listener on the side.  You can sign up and download ngrok here: https://ngrok.com/

# Vulnerabilities
* PHP Type Juggling - Authentication Bypass
* File Upload - Remote Code Execution and File Extension Bypass
* Local File Inclusion - Executing Extension Bypass technique

## PHP Type Juggling
* PHP Loose Comparison - https://www.php.net/manual/en/types.comparisons.php
* Owasp Type Juggling - https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf
* PHP Magic Hashes - https://github.com/spaze/hashes

Vulnerable Code : https://gist.github.com/dreamcast65/1d7fd96893d70d4c85e649b358e47dbc#file-loose-comparison

## File Upload
* File Extension Bypass Cheat Sheet - https://book.hacktricks.xyz/pentesting-web/file-upload

While it may be beneficial to test for other types of file extension bypasses the bypass we will use for this workshop will be .php.png

Vulnerable Code : https://gist.github.com/dreamcast65/c91bd12384d33b2fb4067cd9bc989be0#file-file-upload-bypass
        
Code To make a webshell:

    uploaded_file = "shell.php.png"
    files = {'image':(uploaded_file, "<?php if(isset($_REQUEST['cmd'])){ echo \"<pre>\"; $cmd =($_REQUEST['cmd']);system($cmd);echo \"</pre>\";die;}?>")
	    }
        
## Local file Inclusion
* Owasp LFI - https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion
* LFI cheatsheet - https://highon.coffee/blog/lfi-cheat-sheet/

Vulnerable Code : https://gist.github.com/dreamcast65/4dbddb89d75eec29383b8497d615eaa3#file-local-file-inclusion

## Important Python Libraries
* Requests - https://requests.readthedocs.io/en/latest/

We will be using the Requests library to create a session object to make GET and POST requests which we will use to log in, upload a file, and access that file.

* Subprocess - https://docs.python.org/3/library/subprocess.html

We will use Subprocess to execute and receive our reverse shell without having to start a netcat listener in another terminal.

* Time - https://docs.python.org/3/library/time.html

The time library will only be used to wait a few seconds for requests and responses to come back.

* Argparse - https://docs.python.org/3/library/argparse.html

This will be used for parsing arguments.

## Useful Burp Extension
* Copy As Python-Requests - https://portswigger.net/bappstore/b324647b6efa4b6a8f346389730df160

# Time To Code

## __init__ 
A Sample class with __init__ method.  This is similar to a constructor in C++ and Java and will help with our arguments.
    
    class Person:  

    # init method or constructor   
    def __init__(self, name):  
        self.name = name  
      
    # Sample Method   
    def say_hi(self):  
        print('Hello, my name is', self.name)  
      
    p = Person('Nikhil')  
    p.say_hi() 

## Solution Script
JuggleMe.py - https://github.com/dreamcast65/JuggleMe/blob/main/JuggleMe.py

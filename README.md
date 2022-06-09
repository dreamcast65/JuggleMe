# JuggleMe

## Link to download Vulnerable server
https://drive.google.com/file/d/1D79WJ7gtECDag9_kxquUoUGX4fDHaJ-t/view?usp=sharing

If you do not have VMware Fusion or VMware Workstation the application is available at https://a74c-66-191-6-214.ngrok.io/Login.php.  You will need to install ngrok to receive your reverse shell and will have to either modify the script or set up ngrok with a netcat listener on the side.

## Vulnerabilities
* PHP Type Juggling - Authentication Bypass
* File Upload - Remote Code Execution and File Extension Bypass
* Local File Inclusion - Executing Extension Bypass technique

## PHP Type Juggling
* PHP Loose Comparison - https://www.php.net/manual/en/types.comparisons.php

Example Code : https://gist.github.com/dreamcast65/1d7fd96893d70d4c85e649b358e47dbc#file-loose-comparison
* Owasp Type Juggling - https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf
* PHP Magic Hashes - https://github.com/spaze/hashes

## Important Python Libraries
* Requests - https://requests.readthedocs.io/en/latest/

We will be using the Requests library to create a session object to make GET and POST requests which we will use to log in, upload a file, and access that file.

* Subprocess - https://docs.python.org/3/library/subprocess.html
* Time - https://docs.python.org/3/library/time.html

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
* Owasp Type Juggling - https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf
* PHP Magic Hashes - https://github.com/spaze/hashes

## Important Python Libraries
* Requests
* Subprocess
* Time

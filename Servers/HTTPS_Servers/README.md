---
layout: default
---

# HTTPS Server Creation

## Certificate Creation 

we need a certificate to create https server
you can create it using the below command 

```
$ openssl req -new -x509 -keyout private_key.pem -out public_cert.pem -days 365 -nodes
Generating a RSA private key
..+++++
.................................+++++
writing new private key to 'private_key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:IN
State or Province Name (full name) [Some-State]:Tamil Nadu
Locality Name (eg, city) []:Chennai
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Vmware ,Inc
Organizational Unit Name (eg, section) []:Tanzu
Common Name (e.g. server FQDN or YOUR name) []:35.222.65.55 <----------------------- this ip should be server ip very important
Email Address []:


```

## HTTPS Python server script 

```
# libraries needed: 
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl , socket

# address set
server_ip = '0.0.0.0'
server_port = 3389

# configuring HTTP -> HTTPS
httpd = HTTPServer((server_ip, server_port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./public_cert.pem',keyfile='./private_key.pem', server_side=True)
httpd.serve_forever()
```

**Important note :** The Server network should allow the port configured 

Start the server 
```
$ python3 https_server.py 
106.198.6.176 - - [24/Oct/2021 15:53:54] "GET / HTTP/1.1" 200 -
106.198.6.176 - - [24/Oct/2021 15:53:57] "GET / HTTP/1.1" 200 -
106.198.6.176 - - [24/Oct/2021 15:54:02] "GET / HTTP/1.1" 200 -

```

Curl External ip output:
```
% curl --cacert /Users/padmanabanpr/Downloads/public_cert.pem --cert-type PEM   https://35.222.65.55:3389
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href=".bash_history">.bash_history</a></li>
<li><a href=".bash_logout">.bash_logout</a></li>
<li><a href=".bashrc">.bashrc</a></li>
<li><a href=".cache/">.cache/</a></li>
<li><a href=".profile">.profile</a></li>
<li><a href=".python_history">.python_history</a></li>
<li><a href=".ssh/">.ssh/</a></li>
<li><a href=".viminfo">.viminfo</a></li>
<li><a href="https_server.py">https_server.py</a></li>
<li><a href="server.pem">server.pem</a></li>
</ul>
<hr>
</body>
</html>

```
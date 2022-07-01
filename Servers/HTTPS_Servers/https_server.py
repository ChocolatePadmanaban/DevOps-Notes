# libraries needed: 
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl , socket, sys

# address set
server_ip = '0.0.0.0'
server_port = int(sys.argv[1])

# configuring HTTP -> HTTPS
httpd = HTTPServer((server_ip, server_port), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./public_cert.pem',keyfile='./private_key.pem', server_side=True)
httpd.serve_forever()
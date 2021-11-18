import os
from http.server import HTTPServer, CGIHTTPRequestHandler# Make sure the server is created at current directory
os.chdir('.')
server_object = HTTPServer(server_address=('', 18080), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()

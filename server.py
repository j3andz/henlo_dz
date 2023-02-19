#!/usr/bin/env python3

import socket
import http.server
import socketserver

PORT = 1485

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com", 80))
localIP = s.getsockname()[0]
s.close()
print('''
  _   _   _____   _   _   _                       _       
 | | | | | ____| | \ | | | |   ___             __| |  ____
 | |_| | |  _|   |  \| | | |  / _ \           / _` | |_  /
 |  _  | | |___  | |\  | | | | (_) |         | (_| |  / / 
 |_| |_| |_____| |_| \_| |_|  \___/   _____   \__,_| /___|
                                     |_____|              
''')
print("Servidor Iniciado en " + localIP + ":" + str(PORT))

Handler = http.server.SimpleHTTPRequestHandler
server = socketserver.TCPServer(('', PORT), Handler)
server.serve_forever()
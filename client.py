#!/usr/bin/python

import sys
import socket 

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the socket to the port where the server is listening
     
HOST='localhost'
PORT=5555

server_address = (HOST, PORT)
print 'Connecting to %s port %s' % server_address
sock.connect(server_address)

while True:

    line = raw_input() 
    print 'Sending "%s"' % line
    sock.sendall(line)

print 'Closing socket'
sock.close()


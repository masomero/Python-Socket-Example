#!/usr/bin/python

import os
import sys 
import socket 
import threading
import thread

def handler(clientsock,addr):
    while 1:
        data = clientsock.recv(BUFSIZ)
        if not data:
            break
        print 'Received: ... ' + data
    clientsock.close()

HOST = '0.0.0.0'
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(ADDR)
serversock.listen(2)
while 1:
    print 'waiting for connection...'
    clientsock, addr = serversock.accept()
    print '...connected from:', addr
    thread.start_new_thread(handler, (clientsock, addr))


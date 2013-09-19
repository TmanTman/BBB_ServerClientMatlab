import socket
import string

address = ('localhost',22085)
mySocket = socket.socket()

mySocket.connect(address)
print("Connected successfully!")
mySocket.send('blah'.encode())
print(mySocket.recv(1024))
import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET refers to address family ipv4
#SOC_STREAM means connection oriented tcp protocol
host="192.168.43.15"
port=12345 #can be any number
s.bind((host,port))
s.listen(1)
c,addr=s.accept() #establish connection with client
print ("established a connection with host",addr)
while True:
    data=c.recv(1024).decode()
    print("Message from client ",data)
    inp=(input("Enter your message "))
    c.send(str.encode(inp))
    print()
c.close()
s.close()

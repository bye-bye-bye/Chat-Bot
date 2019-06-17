import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="192.168.43.15"
port=12345
s.connect((host,port))
print("You may start chatting now")
while True:
    inp=(input("Enter your Message "))
    s.send(str.encode(inp))
    data=s.recv(1024).decode()
    print("Message from server ",data)
    print()
s.close()    

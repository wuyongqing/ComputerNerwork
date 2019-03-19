import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
s.send(b'hello World!')
date=s.recv(1024)
print(date.decode('utf-8'))
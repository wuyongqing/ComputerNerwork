import socket
import threading
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'welcome')
    while True:
        date=sock.recv(1024)
        if not date or date.decode('utf-8')=='exit':
            break 
        print(date.decode('utf-8')) 

    sock.close()
    print('Connection from %s:%s'%addr)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(10)
while True:
    sock,addr=s.accept()
    threading.Thread(target=tcplink,args=(sock,addr)).start()
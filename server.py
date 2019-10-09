import socket
s = socket.socket()
s.bind(('127.0.0.1',5000))
s.listen()
print("waiting for client connection request")
caddr,other = s.accept()
while True:
    info = caddr.recv(4096)
    print("client says"info.decode('ascii'))
    data = input("server> ")
    caddr.send(data.encode('ascii'))
caddr.close()
s.close()    
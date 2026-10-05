import socket

s = socket.socket()

server = ('localhost', 3490)

s.connect(server)

while(d := s.recv(100)) != b'':
    print(d.decode(), end='')
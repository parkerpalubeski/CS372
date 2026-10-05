#Parker Palubeski
#CS372
#Project 1 - Web Server

#This is the server-side of the client-server project

import socket
import sys

#Assigns either the passed value or the default of 28333 for the port number and returns it
def assignPort(argv):
    if(len(argv) > 1):
        if(int(argv[1]) < 0 or int(argv[1]) > 65535):
            print("Invalid port number")
            sys.exit()
        else:
            return int(argv[1])
    else:
        return 28333 #default

#Creates the socket from the port number and returns it
def createSocket(port) -> socket:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    return s

def main():
    port = assignPort(sys.argv)
    s =  createSocket(port)
    s.listen()
    while(1):
        new_conn = s.accept()
        new_socket = new_conn[0]
        bytes_received = new_socket.recv(4096)
        print(bytes_received.decode("ISO-8859-1"))
        while("\r\n\r\n" not in bytes_received.decode("ISO-8859-1")):
            bytes_received = new_socket.recv(4096)
            print(bytes_received.decode("ISO-8859-1"))
        bytes_sent = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\nHello!\r\n\r\n"
        new_socket.sendall(bytes_sent.encode("ISO-8859-1"))
        new_socket.close()
        

if __name__ == "__main__":
    main()
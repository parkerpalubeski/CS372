#Parker Palubeski
#CS372
#Project 1 - Web Server


#Usage: python3 webserver.py [PORT NUMBER]

#This is the server-side of the client-server project

import socket
import sys
import mimetypes
import os
from urllib.parse import urlparse

def getpath(url) :
    return urlparse(url)[2]

def get_extension(path: str) -> str:
    root, ext = os.path.splitext(path)
    return root, ext

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
        request_text = bytes_received.decode("ISO-8859-1")
        print(request_text)
        
        lines = request_text.splitlines()
        uri = "/"
        if lines:
            parts = lines[0].split()
            if len(parts) >= 2:
                uri = parts[1]

        path = getpath(uri)
        filename = path.lstrip("/")
        if filename == "":
            filename = "index.html"

        if os.path.exists(filename) and os.path.isfile(filename):
            mime_type, _ = mimetypes.guess_type(filename)
            if not mime_type:
                mime_type = "application/octet-stream"
            
            with open(filename, "rb") as f:
                body = f.read()
            
            header = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\nContent-Length: {len(body)}\r\nConnection: close\r\n\r\n"
            response = header.encode("ISO-8859-1") + body
        else:
            body = b"<html><body><h1>404 Not Found</h1></body></html>"
            header = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: {len(body)}\r\nConnection: close\r\n\r\n"
            response = header.encode("ISO-8859-1") + body

        new_socket.sendall(response)
        new_socket.close()
        

if __name__ == "__main__":
    main()
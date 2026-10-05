import socket

def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("localhost", 3490))
    s.listen()
    while(1):
        client_socket, client_addr = s.accept()
        print(client_addr)
        client_socket.sendall("Some data!\n".encode())
        client_socket.close()

if __name__ == "__main__":
    main()
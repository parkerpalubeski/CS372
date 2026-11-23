# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    server_socket = socket.socket()
    server_socket.bind(("", port))
    server_socket.listen()
    sockets = [server_socket]
    addrs = {}

    while True: #run server
        readable, _, _ = select.select(sockets, {}, {})

        for sock in readable: 
            if sock is server_socket: # connect
                client_socket, _ = server_socket.accept()
                addr = client_socket.getpeername()
                sockets.append(client_socket)
                addrs[client_socket] = addr
                print(f"{addr}: connected")
            else:
                addr = addrs[sock]
                data = sock.recv(4096)
                if not data: #disconnect
                    print(f"{addr}: disconnected")
                    sockets.remove(sock)
                    del addrs[sock]
                    sock.close()
                else: #print received bytes
                    print(f"{addr} {len(data)} bytes: {data}")
    pass

#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
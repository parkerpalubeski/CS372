#Parker Palubeski
#CS372
#Project 1 - Web Client

#This is the client-side of the client-server project. There are honestly a lot of areas this could be cleaned up

import socket
import sys


#Verifies the command line arguments.
#If it is too short, or too long, it exits the program
#If there is no argument for the port number, it defaults to 80
#If all conditions pass and there is an argument for the port number, it returns the port number
#args: argv (list)
#returns: int
def validateInputs(argv) -> int:
    if len(argv) < 2:
        print("Not enough arguments")
        sys.exit()
    elif len(argv) > 4:
        print("Too many arguments")
        sys.exit()
    elif len(argv) == 2:
        return 80
    elif len(argv) == 3 and (int(argv[2]) < 0 or int(argv[2]) > 65536):
        print("invalid port number")
        sys.exit()
    else:
        return int(argv[2])

def main():
    #Error Checks
    portnum = validateInputs(sys.argv)
    host = sys.argv[1]
    s = socket.socket()
    print(f"Host: {host}")
    print(f"Port: {portnum}")
    try:
        s.connect((host, portnum))
    except OSError as error:
        print(f"Connection Failed! {error}")
        sys.exit()

    http_request = (f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n")
    bytes_sent = http_request.encode("ISO-8859-1")
    s.sendall(bytes_sent)


    bytes_received = s.recv(4096)
    print(bytes_received.decode("ISO-8859-1"))
    while len(bytes_received) != 0:
        bytes_received = s.recv(4096)
        print(bytes_received.decode("ISO-8859-1"))
    
    s.close()

    



if __name__ == "__main__":
    main()
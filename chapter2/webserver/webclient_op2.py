from socket import *
import sys

def main():
    argv = sys.argv
    try:
        serverName = argv[1]
        serverPort = int(argv[2])
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        header = 'GET /HelloWorld.html HTTP/1.1\r\nConnection: close\r\n\r\n'
        clientSocket.send(header.encode())
        for i in range(2):
            recv = clientSocket.recv(2048).decode()
            print("recv:\n", recv)
        clientSocket.close()
    except:
        print("Please input parameter (HostName Port)")
        exit()

if __name__ == "__main__":
    main()
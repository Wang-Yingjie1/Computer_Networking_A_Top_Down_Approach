# UDPHeartbeatServer.py
from socket import *
import time
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
serverSocket.settimeout(0.1)   # the value of timeout
recv_time = 0.0

while True:
    try:
        # Receive the client packet along with the address it is coming from 
        message, address = serverSocket.recvfrom(1024)
        serverSocket.sendto(message, address)

        recv_time = time.time()
        message = message.decode()
        time_diff = recv_time - float(message.split()[2])
        print("%2d: %f" % (int(message.split()[1]), time_diff))
    except:
        if recv_time == 0.0:    # client have not started.
            continue
        if time.time() - recv_time > 1.0:
            print("The client is missing")
            break
        else:
            print("Packet loss")

serverSocket.close()
exit()

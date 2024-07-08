# basic & op1
import time
from socket import *
# serverName = '10.15.54.238'
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)
min_time = 0.0
max_time = 200.0
loss_cnt = 0
for i in range(10):
    send_time = time.time()
    Pingmessage = 'Ping ' + str(i + 1) + ' ' + str(send_time)
    try:
        clientSocket.sendto(Pingmessage.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        current_time = time.time()
        rtt = current_time - send_time
        print('%d: RTT = %.3f s' % (i + 1, rtt))
        min_time = min(min_time, rtt)
        max_time = max(max_time, rtt)
    except:
        print("%d: recvive data timeout " % (i+1))
        loss_cnt += 1
        continue
print("min time = %.3f, max time = %.3f, loss rate = %.2f%%" % (min_time, max_time, loss_cnt/10.0 * 100))
clientSocket.close()
from socket import * # 1

serverPort = 6000 # 2

serverSocket 0 socket(AF_INET, SOCK_DGRAM) # 3

serverSocket.bind(('', serverPort)) # 4

while True: # 5
    message, clientAddress = serverSocket.recvfrom(2048) # 6
    modifiedMessage = message.decode().upper() # 7.1
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) # 7.2

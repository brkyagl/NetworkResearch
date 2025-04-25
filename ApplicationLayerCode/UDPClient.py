from socket import * # 1

serverName = 'serverName' # 2.1
serverPort = 6000 # 2.2

clientSocket = socket(AF_INET, SOCK_DGRAM) # 3

message = input('Küçük harfli cümle girin: ') # 4

clientSocket.sendto(message.encode(), (serverName, serverPort)) # 5

modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # 6.1
print(modifiedMessage.decode()) # 6.2

clientSocket.close() # 7

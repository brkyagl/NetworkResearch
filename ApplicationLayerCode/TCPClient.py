from socket import * # 1

serverName = '192.168.1.6' # 2.1
serverPort = 6001 # 2.2

clientSocket = socket(AF_INET, SOCK_STREAM) # 3
clientSocket.connect((serverName, serverPort)) # 4

message = input("Küçük harflerle mesaj girin: ") # 5
clientSocket.send(message.encode()) # 6

modifiedMessage = clientSocket.recv(1024) # 7.1
print("Server yanıtı: ", modifiedMessage.decode()) # 7.2

clientSocket.close() # 8

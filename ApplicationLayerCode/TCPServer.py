from socket import *

serverPort = 6001

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print('Sunucu teslim almaya hazır.')

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    upperMessage = message.upper()
    connectionSocket.send(upperMessage.encode())
    connectionSocket.close()

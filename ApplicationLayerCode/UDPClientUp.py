from socket import *
import sys

serverName = '192.168.1.6' # lhost
serverPort = 6000

clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Client başlatıldı, server'a mesaj göndermeye hazır:", serverName, "port:", serverPort)

while True:

    message = input("Küçük harflerle mesaj girin: ")

    try:

        clientSocket.sendto(message.encode(), (serverName, serverPort))

        clientSocket.settimeout(5.0) # 5 > sn sürerse udp kapalı olabilir.

        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

        print("Server mesajı: ", modifiedMessage.decode())
        print("")

    except TimeoutError:
        print("Yanıt alma süresi doldu (Timeout). Server kapalı olabilir veya erişilemiyor olabilir.")
        break

    except OSError as e:
        print(f"Soket hatası: {e}. Server kapalı olabilir veya erişilemiyor olabilir.")
        break

    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        break

from socket import *
import threading
import signal
import sys
import time 

serverPort = 6000
serverSocket = None
shutdown_event = threading.Event()

def signal_handler(sig, frame):
    print("\nCTRL+C algılandı! Sunucu kapatılıyor...")

    shutdown_event.set()
  
    if serverSocket:
        try:
            serverSocket.close()
        except OSError:
            pass

def run_server_thread():
    global serverSocket 

    print("Sunucu iş parçacığı başlatıldı, paketler bekleniyor...")

    while not shutdown_event.is_set():
        try:
            message, clientAddress = serverSocket.recvfrom(2048)

            if not shutdown_event.is_set():
                modifiedMessage = message.decode().upper()
                serverSocket.sendto(modifiedMessage.encode(), clientAddress)
                print(f"Mesaj alındı from {clientAddress}: {message.decode()}")
                print(f"Yanıt gönderildi to {clientAddress}: {modifiedMessage}")

        except OSError as e:
    
            if shutdown_event.is_set():
                print("Sunucu soketi kapatıldı, iş parçacığı sonlandırılıyor.")
                break 
            else:
                print(f"Sunucu iş parçacığında beklenmeyen soket hatası: {e}")
                break 

        except Exception as e:
            print(f"Sunucu iş parçacığında beklenmeyen hata: {e}")
            break 

    print("Sunucu iş parçacığı duruyor.")

if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)

    try:
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(('', serverPort))
        print(f"UDP sunucusu {serverPort} portunda dinliyor (Ctrl+C ile durdurulabilir)...")
    except OSError as e:
        print(f"Sunucu başlatılırken hata oluştu: {e}")
        sys.exit(1) 

    server_thread = threading.Thread(target=run_server_thread)
    server_thread.start()

    try:
        
        while server_thread.is_alive():
             server_thread.join(timeout=1.0)
    except KeyboardInterrupt:
        print("\nAna iş parçacığında klavye kesintisi algılandı, kapatma sağlanıyor.")
        
        shutdown_event.set()
        
        if serverSocket:
            try:
                serverSocket.close()
            except OSError:
                pass
        server_thread.join() 

    print("Ana program sonlandı!")

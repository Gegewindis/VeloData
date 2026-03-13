from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    gethostbyname,
    gethostname
    )
from Crypto.Cipher import AES
import os
from PySide6.QtCore import QThread

KEY = b"VeloDataTestKey1"
NOISE = b"ThisIsSomeTstSlt"
CIPHER = AES.new(KEY, AES.MODE_EAX, NOISE)

def setUpReciever() -> tuple[socket, int]:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 0))
    port = serverSocket.getsockname()[1]
    serverSocket.listen()

    return (serverSocket, port)

def waitForFiles(serverSocket: socket) -> None:
    pass

def getUserIp() -> str:
    return gethostbyname(gethostname())

def senderConnect(hostName : str | int, port: int) -> socket:
    client = socket(AF_INET, SOCK_STREAM)
    try:
        client.connect((hostName, port))
        return client
    except:
        return None
    
def sendFiles(client: socket, fileSent=None):
    for fileName in os.listdir("Sending_files/"):
        fileSize = os.path.getsize(f"Sending_files/{fileName}")

        with open(f"Sending_files/{fileName}", "rb") as fh:
            data = fh.read()

        data = CIPHER.encrypt(data)

        client.send(fileName.encode())
        client.send(str(fileSize).encode())
        client.send(data)
        client.send(b"<END>")

        if fileSent:
            fileSent(fileName)

        os.remove(f"Sending_files/{fileName}")

class RecieverThread(QThread):
    def __init__(self, serverSocket: socket):
        super().__init__()
        self.running = True
        self.serverSocket = serverSocket

    def run(self):
        while self.running:
            client, addr = self.serverSocket.accept()
            print(client, addr)
    def stop(self):
        self.running = False
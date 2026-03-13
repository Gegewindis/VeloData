from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    gethostbyname,
    gethostname,
    )
from Crypto.Cipher import AES
import os
from PySide6.QtCore import QThread, Signal

KEY = b"VeloDataTestKey1"
NOISE = b"ThisIsSomeTstSlt"
CIPHER = AES.new(KEY, AES.MODE_EAX, NOISE)

def setUpReciever() -> tuple[socket, int]:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 0))
    port = serverSocket.getsockname()[1]
    serverSocket.listen()

    return (serverSocket, port)

def getUserIp() -> str:
    return gethostbyname(gethostname())

def senderConnect(hostName : str | int, port: int) -> socket:
    client = socket(AF_INET, SOCK_STREAM)
    try:
        client.connect((hostName, port))
        return client
    except:
        return None
    
def sendFiles(client: socket, fileSent: callable, sentProgress: callable):
    sentProgress.emit(0)
    fileNames = os.listdir("Sending_files/")
    fileNames.remove(".gitkeep")
    for i, fileName in enumerate(fileNames):
        with open(f"Sending_files/{fileName}", "rb") as fh:
            data = fh.read()

        data = CIPHER.encrypt(data)
        fileNameEncoded = fileName.encode()

        client.send(len(fileNameEncoded).to_bytes(4, "big"))
        client.send(fileNameEncoded)
        client.send(len(data).to_bytes(6, "big"))
        client.send(data)

        fileSent.emit(fileName)
        sentProgress.emit(int(i/len(fileNames)))

        os.remove(f"Sending_files/{fileName}")

class RecieverThread(QThread):
    statusFunc = Signal(str)
    def __init__(self, serverSocket: socket):
        super().__init__()
        self.running = True
        self.connected = False
        self.serverSocket = serverSocket
        self.serverSocket.settimeout(1.0)

    def run(self):
        while self.running:
            if not self.connected:
                try: 
                    client, addr = self.serverSocket.accept()
                    self.connected = True
                    self.statusFunc.emit("green")
                except TimeoutError:
                    continue
            else:
            # Receive filename
                nameSize = int.from_bytes(self.recvAll(client, 4), "big")
                if not nameSize:
                    self.connected = False
                    self.statusFunc.emit("orange")
                else: # If the connection is not active then don't continue
                    fileName = self.recvAll(client, nameSize).decode()

                    # Receive file data
                    dataSize = int.from_bytes(self.recvAll(client, 6), "big")
                    data = self.recvAll(client, dataSize)

                    # Decrypt and save
                    data = CIPHER.decrypt(data)
                    with open(f"Recieved_files/{fileName}", "wb") as fh:
                        fh.write(data)

    def recvAll(self, sock: socket, size: int):
        data = b""
        while len(data) < size:
            chunk = sock.recv(size - len(data))
            if not chunk:
                break
            data += chunk
        return data

    def stop(self):
        self.running = False

class SenderThread(QThread):
    sentStatus = Signal(str)
    sentProgress = Signal(int)
    fileSent = Signal(str)
    def __init__(self, client: socket):
        super().__init__()
        self.client = client

    def run(self):
        try:
            sendFiles(self.client, self.fileSent, self.sentProgress)
        except:
            self.sentStatus.emit("orange")
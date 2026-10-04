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
import shutil
import re

KEY = b"VeloDataTestKey1"
NOISE = b"ThisIsSomeTstSlt" ### NEEDS TO BE RANDOM FOR IT TO BE SECURE
CHUNK_SIZE = 65536 # 4kb

RECIEVED_DIR = "Recieved_files/"
SEND_DIR = "Sending_files/"


_FORBIDDEN = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_RESERVED = {"CON", "PRN", "AUX", "NUL",
             *(f"COM{i}" for i in range(1, 10)),
             *(f"LPT{i}" for i in range(1, 10))}

def _validateName(name: str) -> None:
    if _FORBIDDEN.search(name):
        raise ValueError("Forbidden character in file name")
    if name in (".", ".."):
        raise ValueError("Bad file name")
    if name != name.rstrip(" ."):
        raise ValueError("File name ends with a dot or space")
    if name.split(".")[0].upper() in _RESERVED:
        raise ValueError("Reserved file name")

def setUpReciever() -> tuple[socket, int]:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 0))
    port = serverSocket.getsockname()[1]
    serverSocket.listen()
    return (serverSocket, port)

# def encrypt(data: bytes) -> bytes:
#     cypher = AES.new(KEY, AES.MODE_EAX, NOISE)
#     data = cypher.encrypt(data)
#     return data

# def decrypt(data: bytes) -> bytes:
#     cypher = AES.new(KEY, AES.MODE_EAX, NOISE)
#     data = cypher.decrypt(data)
#     return data

def getUserIp() -> str:
    return gethostbyname(gethostname())

def senderConnect(hostName : str | int, port: int) -> socket:
    client = socket(AF_INET, SOCK_STREAM)
    try:
        client.connect((hostName, port))
        return client
    except:
        return None
    


class RecieverThread(QThread):
    statusFunc = Signal(str)
    downloadFunc = Signal(object)
    def __init__(self, serverSocket: socket):
        super().__init__()
        self.running = True
        self.connected = False
        self.serverSocket = serverSocket
        self.serverSocket.settimeout(1.0)
        self.client = None

    def run(self):
        try: 
            while self.running:
                if not self.connected:
                    try: 
                        self.client, addr = self.serverSocket.accept()
                        self.client.settimeout(1.0)
                        self.connected = True
                        self.statusFunc.emit("green")
                    except TimeoutError:
                        continue
                    except OSError:
                        break    
                else:
                    try:
                        size = self.recieveFile(self.client)
                        self.downloadFunc.emit(size)
                    except InterruptedError:                 # stop() was called
                        break
                    except Exception as e:
                        #self.errorOccurred.emit(str(e))   # later
                        print(str(e))
                        self.statusFunc.emit("orange")
                        self.connected = False
                        self.client.close()
                        self.client = None

        finally:
            if self.client:           # the worker closes its own socket on the way out
                self.client.close()
                self.client = None

    def recieve(self, sock: socket, size: int) -> bytes:
        data = bytearray()
        while len(data) < size:
            if not self.running:
                raise InterruptedError
            try:
                chunk = sock.recv(min(size - len(data), CHUNK_SIZE))
            except TimeoutError:
                continue

            if not chunk:
                raise ConnectionError("Peer closed connection")
            
            data.extend(chunk)
        return bytes(data)

    def recieveHeader(self, sock: socket) -> tuple[str, int]:
        nameSize = int.from_bytes(self.recieve(sock, 1), "big")
        fileName = self.recieve(sock, nameSize).decode()
        fileSize = int.from_bytes(self.recieve(sock, 6), "big")

        if fileSize > shutil.disk_usage(RECIEVED_DIR).free:
            raise ValueError("Not enough disk space")

        if nameSize <= 0:
            raise ValueError("Bad name length")

        _validateName(fileName)
        
        return (fileName, fileSize)

    def recieveFile(self, sock: socket) -> int:
        fileName, fileSize = self.recieveHeader(sock)
        header = len(fileName.encode()).to_bytes(1, "big") + fileName.encode() + fileSize.to_bytes(6, "big")

        nonce = self.recieve(sock, 16)
        cypher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
        cypher.update(header)

        finalPath = RECIEVED_DIR + fileName
        tempPath = finalPath + ".part"

        try:
            with open(tempPath, "wb") as fh:
                remaining = fileSize
                while remaining > 0:
                    data = self.recieve(sock, min(CHUNK_SIZE, remaining))
                    fh.write(cypher.decrypt(data))
                    remaining -= len(data)
            tag = self.recieve(sock, 16)
            cypher.verify(tag)
            os.replace(tempPath, finalPath)
        except BaseException:
            try:
                os.remove(tempPath)
            except OSError:
                pass
            raise

        return fileSize

    def stop(self) -> None:
        self.running = False
class SenderThread(QThread):
    sentStatus = Signal(str)
    sentProgress = Signal(str)
    removeFile = Signal(str)
    def __init__(self, client: socket):
        super().__init__()
        self.client = client

    def run(self):
        self.sendFiles(self.client, self.removeFile, self.sentProgress)

    def sendFiles(self, client: socket, removeFile: callable, sentProgress: callable) -> None:
        fileNames = os.listdir("Sending_files/")
        fileNames.remove(".gitkeep")
        sentProgress.emit(f"0/{len(fileNames)}")
        for i, fileName in enumerate(fileNames):
            filePath = SEND_DIR + fileName
            fileSize = os.path.getsize(f"Sending_files/{fileName}")
            nameBytes = fileName.encode()
            header = len(nameBytes).to_bytes(1, "big") + nameBytes + fileSize.to_bytes(6, "big")

            cypher = AES.new(KEY, AES.MODE_EAX)
            cypher.update(header)

            client.sendall(header)
            client.sendall(cypher.nonce)

            with open(f"Sending_files/{fileName}", "rb") as fh:
                while data := fh.read(CHUNK_SIZE):
                    try:
                        client.sendall(cypher.encrypt(data))
                    except ConnectionError:
                        self.sentStatus.emit("orange")
                        return

            tag = cypher.digest()
            client.sendall(tag)

            removeFile.emit(fileName)
            sentProgress.emit(f"{str(i + 1)}/{str(len(fileNames))}")
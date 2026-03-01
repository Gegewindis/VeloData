from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    gethostbyname,
    gethostname
    )


def setUpReciever() -> tuple[socket, int]:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 0))
    port = serverSocket.getsockname()[1]
    serverSocket.listen(2)

    return (serverSocket, port)

def waitForFiles(serverSocket) -> None: ### Needs multithreading to work and needs to check a variable
    while True:      
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(2048).decode()

def getUserIp() -> str:
    return gethostbyname(gethostname())
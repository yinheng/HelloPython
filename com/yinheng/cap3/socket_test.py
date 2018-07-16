import socket
import threading

def start_server():
    s = socket.socket()
    print(s)
    host = socket.gethostname()
    print(host)
    port = 1234

    s.bind((host, port))
    s.listen(9)

    while True:
        c, addr = s.accept()
        c.send(bytes("Hello I am server", encoding = "utf8"))
        c.close()

def start_client():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))
    print(str(s.recv(2048), encoding = "utf-8"))
    s.close()

threading.Thread(target=start_server).start()
threading.Thread(target=start_client).start()


import socket
from threading import Thread

def new_server_incoming(addr, conn):
    print("New incoming P2P connection from", addr)
    # Hoàn thiện đơn giản: Nhận dữ liệu và trả OK
    data = conn.recv(1024)
    print("Received data:", data.decode())
    conn.send(b"Transfer OK")
    conn.close()

def thread_server(host, port):
    print("Thread server listening on {}:{}".format(host, port))
    serversocket = socket.socket()
    serversocket.bind((host, port))
    serversocket.listen()
    while True:
        conn, addr = serversocket.accept()
        nconn = Thread(target=new_server_incoming, args=(addr, conn))
        nconn.start()

# Để test, chạy thread_server("0.0.0.0", 33557)
import socket
from threading import Thread

def new_connection(addr, conn):
    print("New connection from", addr)
    # Có thể thêm xử lý dữ liệu ở đây (minh họa)
    data = conn.recv(1024)
    print("Received:", data.decode())
    conn.send(b"OK")
    conn.close()

def get_host_default_interface_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def server_program(host, port):
    serversocket = socket.socket()
    serversocket.bind((host, port))
    serversocket.listen(10)
    while True:
        conn, addr = serversocket.accept()
        nconn = Thread(target=new_connection, args=(addr, conn))
        nconn.start()

if __name__ == "__main__":
    port = 22236
    host = get_host_default_interface_ip()
    print("Listening on:", host, port)
    server_program(host, port)
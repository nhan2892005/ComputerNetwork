import socket
from threading import Thread

peers = []  # Hoàn thiện: List lưu peers

def new_connection(addr, conn):
    print("New connection from", addr)
    data = conn.recv(1024).decode()
    if data.startswith("send_info"):
        _, peer_ip, peer_port = data.split(",")
        peers.append((peer_ip, int(peer_port)))
        conn.send(b"OK")
    elif data.startswith("get_list"):
        list_str = ";".join([f"{ip}:{port}" for ip, port in peers])
        conn.send(list_str.encode())
    else:
        conn.send(b"Invalid command")
    conn.close()

def get_host_default_interface_ip():
    # Tương tự server.py
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
    serversocket.listen()
    while True:
        conn, addr = serversocket.accept()
        nconn = Thread(target=new_connection, args=(addr, conn))
        nconn.start()

if __name__ == "__main__":
    port = 22236
    host = get_host_default_interface_ip()
    print("Listening on {}:{}".format(host, port))
    server_program(host, port)
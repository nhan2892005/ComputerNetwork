import socket
from threading import Thread

def new_connection(data, addr, server_socket):
    print("Received from {}: {}".format(addr,data.decode()))

def get_serverhost_default_interface_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
       s.connect(('8.8.8.8',1))
       ip = s.getsockname()[0]
    except Exception:
       ip = '0.0.0.0'
    finally:
       s.close()

    return ip

def start_udp_server(host='0.0.0.0', port=9999):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("UDP Server listening on {}:{}".format(host,port))

    while True:
        data, addr = server_socket.recvfrom(1024)
        thread = Thread(target=new_connection, args=(data, addr, server_socket))
        thread.start()

if __name__ == "__main__":
    hostip = get_serverhost_default_interface_ip()
    port = 22236

    start_udp_server(hostip, port)
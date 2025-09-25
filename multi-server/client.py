import socket
import time
import argparse
from threading import Thread

def new_connection(tid, host, port):
    print("Thread ID {} connecting to {}:{}".format(tid, host, port))
    client_socket = socket.socket()
    client_socket.connect((host, port))
    client_socket.send(b"Hello from client")
    resp = client_socket.recv(1024)
    print("Response:", resp.decode())
    time.sleep(0.3)  # Demo sleep
    client_socket.close()
    print("OK! I am ID={} done here.".format(tid))

def connect_server(threanum, host, port):
    threads = [Thread(target=new_connection, args=(i, host, port)) for i in range(threanum)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-ip", required=True)
    parser.add_argument("--server-port", type=int, required=True)
    parser.add_argument("--client-num", type=int, default=1)
    args = parser.parse_args()
    connect_server(args.client_num, args.server_ip, args.server_port)
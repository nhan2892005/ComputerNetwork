import socket

def thread_client(id, serverip, serverport, peerip, peerport):
    print("Thread ID {} connecting to {}:{}".format(id, serverip, serverport))
    client_socket = socket.socket()
    client_socket.connect((serverip, serverport))
    # Hoàn thiện: Gửi send_info (đăng ký peer)
    msg = f"send_info,{peerip},{peerport}"
    client_socket.send(msg.encode())
    resp = client_socket.recv(1024).decode()
    print("Response from tracker:", resp)
    client_socket.close()

# Để test, gọi thread_client(1, "127.0.0.1", 22236, "my_ip", "my_port")
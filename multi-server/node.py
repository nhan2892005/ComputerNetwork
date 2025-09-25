import argparse
from threading import Thread
# Import các function từ các file khác (giả sử cùng folder)
from thread_server import thread_server
from thread_client import thread_client
from thread_agent import thread_agent

def get_host_default_interface_ip():
    # Tương tự ở server.py
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Node connect to predeclared server")
    parser.add_argument("--server-ip", required=True)
    parser.add_argument("--server-port", type=int, required=True)
    parser.add_argument("--agent-path", required=True)
    args = parser.parse_args()

    serverip = args.server_ip
    serverport = args.server_port
    agentpath = args.agent_path

    peerip = get_host_default_interface_ip()
    peerport = 33557  # Port P2P ngẫu nhiên

    tserver = Thread(target=thread_server, args=(peerip, peerport))
    tclient = Thread(target=thread_client, args=(1, serverip, serverport, peerip, peerport))
    tagent = Thread(target=thread_agent, args=(2, agentpath))

    tserver.start()
    tclient.start()
    tclient.join()
    tagent.start()
    tagent.join()
    tserver.join()  # Chạy mãi
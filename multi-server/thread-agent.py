import time
import mmap
import socket  # Để kết nối nếu cần get_list

def thread_agent(time_fetching, filepath):
    while True:
        with open(filepath, "r+") as file_obj:
            with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
                text = mmap_obj.read().decode("utf-8").strip()
                print("Read from shared file:", text)
        # Hoàn thiện đơn giản: Xử lý command
        if text.startswith("#get_list"):
            # Giả sử kết nối tracker để lấy list (thay "tracker_ip", "tracker_port" bằng thực tế)
            client = socket.socket()
            client.connect(("127.0.0.1", 22236))
            client.send(b"get_list")
            resp = client.recv(1024).decode()
            client.close()
            print("Got list:", resp)
            # Viết lại file để confirm
            with open(filepath, "w+") as wfile_obj:
                wfile_obj.truncate(0)
                with mmap.mmap(wfile_obj.fileno(), 0, access=mmap.ACCESS_WRITE) as mmap_wobj:
                    mmap_wobj.write(b"done")
        time.sleep(time_fetching)

# Để test, thread_agent(2, "shared_file.txt")
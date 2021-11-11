import socket

class udp:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = "first msg"
        self.sock.sendto(msg.encode('utf-8'), ('127.0.0.1', 12345))

    def listen(self):
        data,addr = self.sock.recvfrom(4096)
        msg = data.decode('utf-8')
        
        return float(msg)

    def close(self):
        self.sock.close()
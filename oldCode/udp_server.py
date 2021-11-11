import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv.bind(('127.0.0.1', 12345))
data,addr=serv.recvfrom(4096)

for i in range(1, 1000):
    print(str(data))
    serv.sendto(str(i/500.0).encode('utf-8'), addr)
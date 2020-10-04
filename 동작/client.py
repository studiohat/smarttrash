# -*- coding: utf8 -*-
import socket
import time

## TCP 사용
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("사용")
## server ip, port
s.connect(('192.168.1.11', 9001))
print("연결")

while True:
    f = open("D:/text1.txt", "r")
    line = f.readline()
    s.sendall(line.encode())


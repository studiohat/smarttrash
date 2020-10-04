import socket
import os,sys
import time 
 
HOST="192.168.1.11"
PORT=9001
 
#TCP 사용
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
 
#서버의 아이피와 포트번호 지정
s.bind((HOST,PORT))
print('Socket bind complete')
# 클라이언트의 접속을 기다린다. (클라이언트 연결을 10개까지 받는다)
s.listen(10)
print('Socket now listening')
 
#연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn,addr=s.accept()
 
print("Socket go")
while True:
  data = conn.recv(1024)
  if(data.decode() == "can"):
      EXPORT = "python /home/pi/motor_test.py"
      os.system(EXPORT)
      
  time.sleep(1)
  print("1")
  

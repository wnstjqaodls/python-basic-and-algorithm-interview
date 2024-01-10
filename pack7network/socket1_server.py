# 단순서버 구축 : 클라이언트의 요청에 1 회만 반응
from socket import *
serversock = socket(AF_INET, SOCK_STREAM) # socket ( 소켓종류 , 소켓유형)
serversock.bind(('127.0.0.1',8888)) # 소켓을 컴 주소에 바인딩
serversock.listen(1)   # 1~ 5 까지 가능  동시접속가능수. 클라이언트와의 연결정보수
print('서버 서비스 시작...')

conn , addr = serversock.accept()
print('client addr : ', addr)
print('from client msg : ',conn.recv(1024).decode())
conn.close()
serversock.close()
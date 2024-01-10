#client 소스
from socket import *

clientsock = socket(AF_INET,SOCK_STREAM)
clientsock.connect(('127.0.0.1',8888))  #해당 주소로 능동적으로 접속 시도
clientsock.send('안녕 바나나'.encode(encoding='utf-8', errors='strict'))

clientsock.close()
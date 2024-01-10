# clien source

from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.5', 7777))  # 해당 주소로 능동적으로 접속 시도
clientsock.send('하이 반가워'.encode(encoding='utf-8'))
re_msg = clientsock.recv(1024).decode()
print('수신된 자료 : ', re_msg)

clientsock.close()

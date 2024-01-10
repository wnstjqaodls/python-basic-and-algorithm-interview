# 네트워크를 위한 통신채널 socket 으로 제공

import socket

print(socket.getservbyname('http','tcp'))
print(socket.getservbyname('telnet','tcp'))
print(socket.getservbyname('ftp','tcp'))
print(socket.getservbyname('smtp','tcp'))
print(socket.getservbyname('pop3','tcp'))

print()
print(socket.getaddrinfo('www.naver.com', 80, proto= socket.SOL_TCP))

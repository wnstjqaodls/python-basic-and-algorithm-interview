#SimpleHTTPRequestHandler 를 확장한 클래스 사용 
#클라이언트의 정보를 받아 처리하고 , py 파이릉ㄹ 호출 가능 
from http.server import CGIHTTPRequestHandler, HTTPServer


port = 7878

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin']
    
    

serv = HTTPServer(('127.0.0.1', port), Handler)

print('웹서비스 출발........')
serv.serve_forever()  #무한루프에 빠트림

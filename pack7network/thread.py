#thread 스레드는 프로세스와 유사하나 같은 프로세스 내에서 수행됨 같은 실행환경을  공유하ㅓㄴ다는
#점에서 프로세스와 다르다


import threading,time

def run(id):
     for i in range(1,11):
         print('id{} > {}'.format(id,i))
         time.sleep(0.5)
         
         
#  스레드를 사용하지 않는 경우

"""run('일')
run('둘')
"""

#스레드를 사용한 경우
th1 = threading.Thread(target=run , args=('하나',))
th2 = threading.Thread(target=run , args=('둘',))
th1.start()
th2.start()

th1.join()  # 사용자 정의 스레드가 종료 될 때까지 메인스레드 대기
th2.join()

print('프로그램 종료')
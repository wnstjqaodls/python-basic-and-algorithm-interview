#thread 간 공유자원 값 충돌방지
import threading
import time

g_count =0 
lock = threading.Lock()

def threadCount(id,count):
    global g_count
    for i in range(count):
        lock.acquire() # 락을 걸어 특정스레드가 공유자원 사용하늗동안 다른스레드중지
        print('id %s==> count :%s, g_count:%s'%(id,i,g_count))
        g_count =g_count +1
        lock.release() #lock 해제
        
        
for i in range(1,6):
    threading.Thread(target=threadCount, args=(i,5)).start()
    

time.sleep(1)
print('최종 g count :' , g_count)
print('finish')
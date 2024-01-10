# 데이터 연동 프로그래밍
#개인용 DBMS : sqlite <= 파이썬 설치시 자동등록 기본모듈(라이브러리) 로 제공
import sqlite3
print(sqlite3.sqlite_version)

print()
#conn = sqlite3.connect('exam.db') # db 파일을 생성한다
conn = sqlite3.connect(':memory:') # ram 파일생성한다 = 파일생성안하게된다, 테스트용 프로그램끝나면 사라짐!

try:
    cur = conn.cursor()       # SQL 처리 가능 객체 
    
    cur.execute('create table if not exists friends(name text,phone text,addr text)')
    cur.execute("insert into friends(name,phone,addr) values('한국인','111-1111','seoul강남구')")
    cur.execute("insert into friends values('한국인2','222-1111','seoul강남구')")
    inputdata = ('유비','333-3333','그동네')
    cur.execute('insert into friends values(?,?,?)',inputdata)
    conn.commit()
    
    #select
    cur.execute("select * from friends") # select 의 결과를 커서가 기억함
    #print(cur.fetchone())
    print(cur.fetchall()) 
    
    
except Exception as e:
    print('err: ',e)
finally:
    cur.close()
    conn.close()
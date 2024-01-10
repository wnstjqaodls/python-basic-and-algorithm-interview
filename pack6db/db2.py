# sqlite 사용  개인용 데이터 베이스임
import sqlite3


def dbProcess(dbName):
    #print(dbName)
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        
        cursor.execute("drop table if exists junsub")
        cursor.execute("create table if not exists junsub(id integer primary key, name text)") # 정수일땐 integer  실수일때 real
        
        #insert
        cursor.execute("insert into junsub values(1,'김준섭')")
        
        #tdata = (2,'고길동) # tuple
        tdata = 2, '고길동' #tuple
        cursor.execute('insert into junsub values(?,?)',tdata)
        
        ldata = [3,'공기밥'] #list    set type은 안됨! 
        cursor.execute('insert into junsub values(?,?)',ldata)
        
        dicdata = {'id':4 ,'name' : '고래밥'} # dict 타입
        cursor.execute('insert into junsub values(:id,:name)',dicdata)
        
        dicdata = {'sabun':5 ,'irum' : '고래밥'} # dict 타입     컬럼의 이름과맞추는게아니라 dict의 key 와 맞추는거임
        cursor.execute('insert into junsub values(:sabun,:irum)',dicdata)
        
        #select
        print('출력 1')
        cursor.execute("select * from junsub")
        for r in cursor:
            print(str(r[0])+ ' ' + r[1])
            
        
        print('출력 2----------')
        #cursor.execute("select * from junsub where id <=2")
        #inputid =2
        #cursor.execute("select * from junsub where id <=%d"%inputid)
        
        inputname = '홍길동'
        cursor.execute("select * from junsub where name = '%s'"%inputname) # %s는   ' ' 작따를 넣어야하는것 주의
        
        
        for r in cursor.fetchall():
            print(str(r[0])+ ' ' + r[1])
            
        print('출력 3 - sql 함수 -------')
        cursor.execute("select count(*) from junsub")
        #print('건수 :' + str(cursor.fetchone()))
        print('건수 :' + str(cursor.fetchone()[0])) 
            
        
        
        
            
            
    except Exception as e:
        print('err' ,e)
        
    finally:
        pass
    
    
if __name__ == '__main__':
    dbProcess('test.db')
    
    
    
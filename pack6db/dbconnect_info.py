import MySQLdb

config = {

    'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'test',

    'port':3307,
    'charset':'utf8',

    'use_unicode':True

}
import pickle
with open('mydb.dat','rb')as obj:
    config = pickle.load(obj)
    
def chulbal():
    try:
        conn = MySQLdb.connect(**config)       # dict type 때문에 **을 쓴다 내용전부를 담기위해
        cursor = conn.cursor()
        
        buser_no = input('부서번호 입력:')
        #buser_no = 10
        sql = """
            select jikwon_no,jikwon_name,buser_num,jikwon_pay
            from jikwon
            where buser_num = {0}
        """.format(buser_no)
        #print(sql)
        cursor.execute(sql)
        datas = cursor.fetchall()
        #print(datas,len(datas))
        
        if len(datas) == 0:
            print(str(buser_no + '벤 부서는 없어요'))
            return 
        
        for jikwon_no,jikwon_name,buser_num,jikwon_pay in datas:
            print(jikwon_no,jikwon_name,buser_num,jikwon_pay)
        
    except Exception as e:
        print('err' ,e)
        
    finally:
        cursor.close()
        conn.close()
        
        
if __name__ == '__main__':
    chulbal()        
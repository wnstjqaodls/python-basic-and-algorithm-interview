#키보드에서 부서번호를 입력받아 해당 부서 직원자료 출력!
import MySQLdb


conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test', port =3307)
print(conn)
conn.close


config = {

    'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'test',

    'port':3307,
    'charset':'utf8',

    'use_unicode':True

}

def chulbal():
    try:
        conn = MySQLdb.connect(**config)       # dict type 때문에 **을 쓴다 내용전부를 담기위해
        cursor = conn.cursor()
        
        #buser_no = input('부서번호 입력:')
        buser_no = 10
        sql = """
            select jikwon_no,jikwon_name,buser_num,jikwon_pay
            from jikwon
            where buser_num = {0}
        """.format(buser_no)
        print(sql)
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)
        
        
        
        
    except Exception as e:
        print('err' ,e)
        
    finally:
        cursor.close()
        conn.close()
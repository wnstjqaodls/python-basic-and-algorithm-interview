#원격 데이터베이스 연동 프로그래밍 : mariaDB
# pip install mysqlclient
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

try:
    conn = MySQLdb.connect(**config)       # dict type 때문에 **을 쓴다 내용전부를 담기위해
    
    cursor = conn.cursor()
    
    #자료 추가
    """
    sql = "insert into sangdata(code,sang,su,dan) values(%s,%s,%s,%s)"
    sql_input_data = ('10','아메리카노',5,5000)
    cursor.execute(sql,sql_input_data)
    conn.commit()
    """
    
    #자료 수정
    """sql = "update sangdata set sang=%s,su=%s,dan=%s where code=%s"
    sql_update_data = ('콜드브루',25,6000,'10')
    result = cursor.execute(sql,sql_update_data)
    print('result: ', result )
    conn.commit()
    """
    
    #자료 삭제
    """    sql = "delete from sangdata where code=%s"
    sql_delete_data = '10'
    result = cursor.execute(sql,(sql_delete_data,))
    if result == 0:
        print('삭제자료 없어용')
    else:
        print('삭제 성공')
    conn.commit()"""
    
    
    
    #자료읽기
    sql = "select * from sangdata"
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        print(data)
        #print('%s %s %s %s'%data) # 결과에 괄호를 벗기고싶을 때 
        
    print()
    for aa in cursor:
        print(aa[0],aa[1],aa[2],aa[3])
        
    print()
    for (code,sang,su,dan) in cursor:
        print(code,sang,su,dan)
        
    print()
    for (a,b,c,d) in cursor:
        print(a,b,c,d)
        
except Exception as e:
    print('err' , e)
    
finally:
    cursor.close()
    conn.close()
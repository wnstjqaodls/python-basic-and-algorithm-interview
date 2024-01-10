# 예외처리 : 파일 , 네트워크 , 키보드 , DB연동 , 나누기 ... 등의 작업을 하다가 에러가 발생한경우 대처!

def divide(a,b):
    return a / b

#c = divide(5,0) # 에러가 뜨게된다
#print(c)


#에러에 대한 대처 작업 : try ~ except


try:
    x = 9
    c = divide(5,2)
    print(c)
    
    aa = [1,2]
    print(aa[0])
   # print(aa[5])

    f = open("c:/work/abcvxc.txt")
    
except Exception as e:
    print('에러 발생 :',e)
    
except ZeroDivisionError:
    print('에러발생 두번째숫자는 0 을 주면안됩니다')

except IndexError as e:
    print('참조 범위 오류 :' ,e)

finally:
    print('에러에 상관없이 반드시 수행됨')
    del x 
    
        
print('다음 작업 계속')



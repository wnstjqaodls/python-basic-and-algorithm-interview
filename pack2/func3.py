# 변수의 생존 범위, scope rule 
# 접근순서 : Local > Enclosing function > Global 

player = '전국대표' # 전연벽수

def funcSoccer():
    name = '신기해' # 지역변수
    player2 = '조기 축구 선수 대표'
    print(name , player)

#참고 둘은 다른것임!    
aa =funcSoccer # 함수의 주소 치환
print(aa)
aa2 = funcSoccer() #함수의 수행결과를 치환
print(aa2)

print('-----')
funcSoccer()

print(player)

print('***'*10)
a = 10; b = 20; c = 30
print('처리1:a:{},b:{},c:{}'.format(a,b,c ))
def foo():
    a = 40
    b = 50
    def bar(): #함수 내에 함수선언
        #c = 60
        global c
        nonlocal b 
        print('처리2:a:{},b:{},c:{}'.format(a,b,c ))
        c = 60
        b = 70
        
    bar()
    print('처리3:a:{},b:{},c:{}'.format(a,b,c ))
    
foo()
print('처리4:a:{},b:{},c:{}'.format(a,b,c ))
(lambda m,n: m + n)
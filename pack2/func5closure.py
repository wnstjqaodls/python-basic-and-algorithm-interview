# 클로저 (closure) : scope에 제약을 받지 않는 변수들을 포함하고있는 코드블록이다.
# 함수 내의 지역변수를 함수 밖에서 참조를 가능하게함
from sympy.physics.units import amount
from pack1.test7if import result



#선행학습
def funcTimes(a,b):
    c= a * b 
    print(c)
    return c
    
print(funcTimes(2,3))
kbs = funcTimes(2, 3)
print(kbs)

kbs = funcTimes
print(kbs)
print(kbs(2, 3))
print(id(funcTimes) , id(kbs))

del funcTimes       # 참조하고있는 함수의 이름과 주소 을지우는것.  
print(kbs(2, 3))

mbc =sbs = kbs
print(mbc(3,4))
print(sbs(3,4))

print()
print('----클로저 사용하지 않은 경우---')
def out():
    count = 0 
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())
    
out()
out()

print()
print('----클로저 사용한 않은 경우---')
def outer():
    count = 0 
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # 요게바로 클로져 


#print(outer())
var1 = outer()
print(var1())
print(var1())
print(var1())

var2 = outer()
print(var2())
print(var2())
print()
print(id(var1),id(var2))

print('수량 * 단가* 세금을 출력하는 함수 작성 ')
def outer2(tax):
    def inner2(su,dan):
        amount = su* dan * tax
        return amount
    return inner2

#1 분기에는 tax 가 0.1로 부과
q1 = outer2(0.1)
result1 = q1(5,50000)
print('result1:',result1)
result2 = q1(2,10000)
print('result2:',result2)


q1 = outer2(0.05)
result3 = q1(5,50000)
print('result3:',result3)
result4 = q1(2,10000)
print('result4:',result4)

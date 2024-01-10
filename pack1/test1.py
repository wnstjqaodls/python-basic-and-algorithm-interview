'''
Created on 2021. 9. 29.
여러줄 주석임 
@author: subkim
'''
from comtypes.GUID import binary
from sqlalchemy.sql.expression import false

#한줄 주석임 #샾은 한줄주석
var1 = '안녕 파이썬!'
print(var1)
var1 = 3; print(var1)


a= 10
print(a,'',id(a),'',type(a))
b= 10.5
print(a,'',id(b),'',type(b))
c= "python"
print(c,'',id(c),'',type(c))

d= True
print(d,'',id(d),'',type(d))

A = 10
a = 10
b = 10
print('주소비교',a == b, '값비교:', a is b)

print('--------')
print(10, '',oct(10),'',hex(10),'',bin(10))
print(10  ,0o12,  0xa,  0b1010)

print('\n--------')
print(3 , type(3))
print(3.1 , type(3.1))
print(3 + 4j , type(3 + 4j))
print(False, type(False))
print('a' , type(3))
print(())
#묶음형 자료형 
print((1,), type((1,)))
print([1] , type([1]))
print({1} , type(({1}))
#print({'key':1},type({'key':1})) 에러뜸 !! 
# tuple : list와 유사하나 읽기전용 - 속도가 빠름
t = (1,2,3,4,3)     #괄호를 빼도된당
print(t, type(t), len(t))
print(t.count(3), t.index(4))
print(t[0], t[0:3])
#t[0] = 10 실행불가 . 수정불가


imsi = list(t)
print(imsi, type(imsi))
imsi[0] = 10
t = tuple(imsi)
print(t , type(t))
aa = (1)
print(aa, type(aa)) #주의 ! int 임
bb = (1,)
print(bb,type(bb)) # 주의! tuple임


print('---' * 10)
# set : 순서X , 중복 X 
a = {1,2,3,1}
print(a , type(a), len(a))
# print(a[0]) set은 슬라이싱불가.. 인덱싱안된다! 

b = {3,4}
print(b)
#print(a + b) set끼린 더핟기안됨
print(a.union(b))
print(a.intersection(b))
print(a | b , a- b , a & b) # 합 , 차  , 교집합! 

a.update({6,7})
print(a)
a.remove(6)
print(a)

li = [1,2,2,3,2,1]
print(li)
s = set(li)
li = list(s)
print(li)


print('----' *10)
# dict : 순서X , 키 : 값의 쌍으로 구성
mydic = dict(k1 = 1, k2= 'mbc', k3= 3.4)
print(mydic,type(mydic))

dic = {'파이썬':'뱀','자바':'커피','spring':'용수철','kbs':9}
print(dic,type(dic),len(dic))
print(dic['자바'])

dic['오라클'] = '예언자'
print(dic)
del dic['오라클']
print(dic)
dic.pop('자바')
print(dic)

dic['spring'] = '웹용프레임워크'
print(dic)
print(dic.keys())
print(dic.values())
print(dic.get('파이썬'))
print(dic['파이썬'])
print('spring' in dic)
print('summer' in dic)




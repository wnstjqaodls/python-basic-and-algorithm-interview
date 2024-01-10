#.조건판단문 if
var = 5

if var >= 3:
    print('크구나')
    print("참일 때")
    #pass 
else:
    print('거짓 일 때')
        
print('end1')

print()

money = 1000
age = 23
if money >= 500:
    item = '사과'
    if age <= 30:
        msg = '와우 젊다'
    else:
        msg = '허걱 나이좀 있네'
else:  
    item = '감'
    if age >= 20:
        msg = '성인'
    else:
        msg = '미성년'
        
print(item,msg)
print('end2')                               

print()
jumsu = 85
if jumsu >= 90:
    print('우수')
else:
    if jumsu >= 70:
        print('보통')
    else:
        print('저조')        

if jumsu >= 90:
    print('우수2')       
elif jumsu >= 70:
    print('보통')
else:
    print('저조2')
print('end3')

print()
print(3+2, str(3) + '2', int(str(3)) + 2)
#jum = int(input('점수 입력:'))
jum = 88
# print(jum, type(jum))
print(jum, type(jum))

if jum >= 90:
    print('good')
elif jum >= 70:
    print('nice')
else:
    print('nomal')        


print()
if 90 <= jum <= 100:
    print('good2')
elif 70 <= jum < 90:
    print('nice2')
else:
    print('nomal2')
    
print()
names = ['홍길동','신선해','이겨라']
if '홍길동' in names:      #not in 도 사용가능
    print('맞음 내친구')
else:
    print('누구니?')
    
print()
a = 'kbs'

'''if a == 'kbs': 
    print(9)'''

b = 9 if a == 'kbs' else 11
print(b)

a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
#PI = 3.14        #대문자로썻을때 final 이런거없이 자바와다름 . 
a = 3 
if a < 5:
    print(0)
elif a < 10:
    print(1)
else :
    print(2)

# 위 코드를 한줄로
print(0 if a < 5 else 1 if a < 10 else 2)

print()
a = 5
result = a * 2 if a > 3 else a + 2
print('result :' + str(result))  #파이썬은 명시적형변환을항ㅎ상해줘야함 오토박싱? 기능이없다. ㅠㅠ




    
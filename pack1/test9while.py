#while 이어서 
# for + if 문 한 줄로 표기

a = 0

while a < 10:
    a += 1
    if a == 5 or a == 7:continue
    if a == 8:break       #continue 사용시 5를 건너뜀. 바로 조건으로 올라가버려서
    print(a)
else:
    print('while 정상 수행')
    
print('while 수행 후 %d'%a)    

#홀수 짝수 확인하기
'''while True:         # True 나  1 이나 1.5나 뭐든 값이있으니까 ture이기때문에 무한루프에 빠진다.
    su = int(input('정수 입력:'))
    if su == 0:
        print('프로그램 종료')
        break
    elif su %2 == 0:
        print('%d는 짝수'%(su))
    elif su %2 == 1:
        print('%d는 홀수'%(su))'''
        
#임의의 숫자 알아내기
import random #난수 발생 모듈
#random.seed(123)
#print(random.random())
#print(random.randint(1, 10))

num = int(random.randint(1, 10))
while True:
    print('1~10 사이의 컴이 가진 예상 숫자 입력:')
    guess = input()
    su = int(guess)
    if su == num:
        print('성공~  ' *5)
        break
    elif su < num:
        print('더큰 수를 입력')
    elif su > num:
        print('더 작은 수를 입력')
5
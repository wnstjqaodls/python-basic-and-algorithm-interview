# range 함수 : 수열 생성
from dask.array.random import random
print(list(range(1,6))) #시작과 끝값
print(list(range(6)))
print(list(range(1,6,1)))
print(list(range(1,6,2)))
print(tuple(range(1,6)))
print(set(range(1,6)))

print()
for i in range(6):
    print(i, end= ' ')
    
print()
for _ in range(6):
    print('hi',end = ' ')
    
print('\n~ 10 까지의 합')
tot = 0
for i in range(1,11):
    tot += i
    
print(tot)
print(sum(range(1,11)))

print()
for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j),end=" ")
    print()

#문제1
tot = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        tot += i 
        print(i)
print('3과 5의 배수의 총 합: ',tot)
print('-----------')

#문제2) 주사위를 두번 던져서 숫자들의 합이 4의 배수가 되는 경우만 출력하라
for i in range(1,7):
    for j in range(1,7):
        if (i + j)% 4 == 0:
            print(i,' ',j)
print()
        
        
print('for 문 사용을 사용 : 주사위를 2회 던져서 나온 숫자들의 합이 3의 배수이면서 동시에 4의 배수가 되는 경우의 i, j 값을 출력하는 코드를 작성하시오.')

for i in range(1,7):
    for j in range(1,7):
        if (i + j)% 4 == 0 and (i + j)% 3 == 0:
            print(i,' ',j)
print()

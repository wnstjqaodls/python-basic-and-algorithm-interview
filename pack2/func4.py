# 함수 : 인수(argument) 매개변수

def showGugu(start,end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력 ')
showGugu(2, 3)
print()
showGugu(3)
print()
showGugu(start= 7, end = 8)
print()
showGugu(end= 8, start = 7)
print()
showGugu(5,end= 6)
print()
#showGugu(start=5, 6) #에러 . 이렇게는안된다.
#showGugu(end= 6, 6)

print('\n가변인수 처리---')
def func1(*ar):
    print(ar)
    
func1('공기밥','김밥','비빔밥')

print()
def func2(a,*ar):
    print(a)
    print(ar)
    
func2('비빔밥')
func2('비빔밥','김밥','공기밥')

print('-----')
def selectProcess(choice,*ar):
    if choice =='add' : 
        imsi =0 
        for i in ar:
            imsi += i
    elif choice == 'mul':
        imsi = 1
        for i in ar:
            imsi *= i
            
    return imsi        

print(selectProcess('add', 12,3,4,5))
print(selectProcess('mul', 12,3,4,5))

print()
def func3(w,h,**other): # **은 dict type인 경우
    print('몸무게:{},키 :{}'.format(w,h))
    print(other)
    
func3(66,177)
func3(66,177,irum='홍길동',nai=23)


print('----')
def func4(a,b,*c,**d):
    print(a,b)
    print(c)
    print(d)
    
    
    
func4(1,2)
func4(1,2,3,4,5)
func4(1,2,3,4,5,m=6,n=7,z=8)

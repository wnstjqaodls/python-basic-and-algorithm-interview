# 재귀함수 : 함수가 자기자신을 호출 - 반복처리가능

def countDown(n):
    if n == 0:
        print('완료')
    else:
        print(n,end=' ')
        countDown(n-1) # 재귀함수
        
countDown(5)

print('1~10 까지의 정수의 합')
def totFunc(su):
    if su == 1:
        print('그만하자')
        return True
    return su + totFunc(su - 1)

result = totFunc(10)
print('합은'+ str(result))

print()
# 5! : 5*4*3*2*1
def factFunc(a):
    if a == 1:return 1
    print(a)
    return a * factFunc(a-1)

print('S!: ',factFunc(5))
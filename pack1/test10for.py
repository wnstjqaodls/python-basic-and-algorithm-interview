#for문 반복문
for i in [1,2,3,4,5]:
    print(i, end = ' ')
    
print()

colors = ['r','g','b']
#colors = {'r','g','b'} #set
for c in colors:
    print('색은 %s'%c , end = ' ')
    
print()
soft = {'java' :'웹용언어', 'python' :'만능언어', 'C':'시스템개발용'}
for i in soft.items():
    print(i)
    print(i[0] + ' ' + i[1]) #java 웹용언어...
    
    
print()
for k in soft.keys():
    print(k,end = ' ')

print()
for v in soft.values():
    print(v, end = " ")

print()
for a , b in soft.items():
    print(a,' ,',b)

print('평균', '분산', '표준편차----')
jum = [6,5,4,7,3.5]
tot = 0
for i in jum:
    tot += i


avg = tot / len(jum)
print('avg =' , avg )

tot = 0
for i in jum:
    tot += (i - avg) ** 2 
var = tot/ len(jum)
print('var :',var)

import math # sqrt 사용위해 필요한 import
print('std:', math.sqrt(var))

print()
for n in[2,3]:
    print('--- {}단'.format(n))
    for su in [1,2,3,4,5,6,7,8,9]:
        print('{0} * {1} = {2}'.format(n,su,n*su))


print()
li = ['a','b','c']
for i,d in enumerate(li):
    print(i,'',d)
    
    
print('continue,break...')
datas = [1,2,3,4,5]
for i in datas:
   # if i == 2:continue
    if i == 2:break
    print(i,end = ' ')
else:
    print('정상 처리')    
print()

print()
li1 = [3,4,5]
li2 = [0.5,1,2]
for a in li1:
    for b in li2:
        print(a + b,end= " ")
        
results = [a + b for a in li1 for b in li2]
print(results)
for d in results:
    print(d, end= ' ')
    
print('정규표현식, for 사용연습 : 다량의문자열을 공백 단위로 분리해 건수 출력')
import re
#웹에서 스크래핑 했다고 가정하자! 크로링했다고가정
ss = '''
넷플릭스 한국 오리지널 드라마 ‘오징어 게임’이 전 세계적으로 돌풍을 일으키자 해외 주요 매체들도 앞다퉈 열풍을 조명하고 있다.
미국 CNN방송은 “정말 죽여준다”며 엄지를 치켜세웠고, 뉴욕포스트는 “전 세계에 대혼란을 일으켰다”고 평했다.
CNN방송은 29일(현지시간) “‘오징어 게임’은 무엇이고 왜 사로잡는가”라는 제목의 기사에서 “넷플릭스의 최신 히트작(오징어 게임)은 정말 죽여준다”고 보도했다.
이어 “오징어 게임이 화제를 불러일으킨다고 말하는 것은 절제된 표현”이라며 ‘오징어 게임’ 흥행이 “한국 영화 ‘기생충’에서 드러났던 것과 매우 비슷한 현상”이라고 평했다.
‘오징어 게임’을 “빚더미 수렁에 깊이 빠진 참가자들이 거액의 상금을 타기 위해 어린이 게임에 참가한다는 내용의 드라마”라며 간략한 줄거리를 소개했다.
'''

print(ss)
ss2 = re.sub(r'[^가-힣\s]','',ss) # \s는 공백을뜻한다. ^는 ~을 제외한이라는뜻
print(ss2)
ss3 = ss2.split(' ')
print(ss3)
cou = {} #단어 횟수를 dict로 저장

for i in ss3:
    if i in cou:
        cou[i] += 1 # 같은 단어가 있으면 누적
    else:
        cou[i] = 1
        
print(cou)

print('\n dict type(사전형)의 변수로 과일 값 계산')
price = {'사과':2000,'감':500, '배':3000}
gogek_tom = {'사과':2,'배':3} #손님이 구매한 과일갯수
bill = sum(price[f] * gogek_tom[f] for f in gogek_tom)
print('과일값 총액 : {}원'.format(bill))

a= 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i %2 == 0: 
        li.append(i)
print(li)

print(list(i for i in a if i % 2 == 0))

print('\n for문 한 줄로 코딩하기')
datas = [1,2,'a',True,3.5]
li = [i * i for i in datas if type(i)== int]
print(li)

print()
datas = {1,1,2,2,3}
li2 = [i *i for i in datas]
print(li2)

print()
id_name = {1:'tom', 2:'james'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
aa = [(1,2),(3,4),(5,6)]
for a,b in aa:
    print(a+b)
    
    
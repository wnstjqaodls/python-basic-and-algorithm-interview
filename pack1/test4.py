# list 자료형 : 순서 O , 변경 O , 중복 O 가능!
a = [1, 2, 3]
b = [10, a, 20.5 , True , '문자열']
print(a)
print(b)
print(id(a) , id(b))

print()
family = ['엄마', '아빠', '나']
family.append('남동생')
family.insert(1,'삼촌')
family.extend(['이모','고모'])
family += ['여동생']
family.remove('나')
print(len(family), family)
print(family.index('삼촌'))
print(family[0], family[-1],family[0:6:2])

print('중첩 리스트')
aa = [1,2,3,['a','b','c'],4,5]
print(aa)
print(aa[0],aa[3],aa[3][1])

print('복사---')
name = ['톰','제임스','존']
print(name,id(name))
name2 = name
print(name2,id(name2))

import copy
name3 = copy.deepcopy(name) #깊은 복사 . 주소가다름!.. 새로운 객체 생성
print(name3, id(name3))

print()
name[0] = '홍길동'
print(name, id(name))
print(name2, id(name2))
print(name3, id(name3))

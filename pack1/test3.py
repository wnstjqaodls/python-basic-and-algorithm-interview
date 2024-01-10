# 묶음형 자료형 : set - 순서를 갖음, 수정불가 : 슬라이싱가능
s = 'sequence'
print(s)
print(len(s),s.count('e'),s.find('e'),s.find('e',3),s.rfind('e'))
print(s.startswith('s'),s.startswith('a'))
print()
ss = 'mbc'
print(ss,id(ss))
ss = 'abc'
print(ss,id(ss))
# 아예 새로운 객체를 참조한것이다.  수정된것이아님!

print('슬라이싱---')
print(s[0],s[2:4],s[:3],s[3:])
print(s[-1],s[-4:-1],s[-4:])
print(s[1:7:2])
print(id(s))
#s[0] = 'k' 수정불가! 

print()
s2 = 'kbs mbc'
print(s2)
s3 = s2.split(sep= ' ')
print(s3)
s4 = ''.join(s3)
print(s4)
s5= s4.replace('kbs','jtbc')
print(s5)
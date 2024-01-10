#클래스로 새로운 타입 선언하기 : 가수 클래스(설계도) --> 객체 생성
print('뭔가를 하다가~')

class Singer:
    title_song= '파이팅 코리아'
    
    def sing(self):
        msg = '노래는 '
        print(msg, self.title_song,'라라라~')
        
bts = Singer()
print(type(bts))


bts.sing()
bts.title_song = '버터'
bts.sing()
bts.co = '빅히트 엔터테인먼트'
print('소속사 : ', bts.co)

print()
blackpink = Singer()
print(type(blackpink))
blackpink.sing()


print(id(bts))
print(id(blackpink))

# 로또 번호 생성 : 클래스의 포함 연습
import random
from Cython.Compiler.Naming import self_cname

class LottoBall:
    def __init__(self,num): # LottoMachine 의 부품으로 사용
        self.num = num
        

class LottoMachine:
    def __init__(self):
        self.ballList = []  # 로또볼이 기억될 리스트
        for i in range(1,46):
            self.ballList.append(LottoBall(i))
            
    def selectBall(self):

        for a in range(45): # 공을 섞기 전에 확인 하기
            print(self.ballList[a].num, end = ' ')
        
        random.shuffle(self.ballList)
        
        print()
        for a in range(45): # 공을 섞은 후에 화깅ㄴ하기
            print(self.ballList[a].num, end = ' ')
        
        return self.ballList[0:6]

class LottoUiUx:
    def __init__(self):
        self.machine = LottoMachine()   # 클래스의 포함
        
    def playLotto(self):
        input('로또번호를 생성하려면 엔터키를 누르세요')
        selectedBalls = self.machine.selectBall()
        print('\n행운의 번호 : ')
        for b in selectedBalls:        
            print('%d'%b.num, end = ' ')
            
if __name__ == '__main__':
    #LottoUiUx().playLotto()
    lo = LottoUiUx()
    LottoUiUx.playLotto(lo)
#추상 클래스

from abc import *

class Friend(metaclass = ABCMeta):
    def __init__(self,name):
        self.name = name
        
    @abstractclassmethod
    def hobby(self):
        pass
    
    def printName(self):
        print('이름은 ', self.name)
        
class John(Friend):
    def __init__(self,name,addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self):
        print(self.addr + '거리를 걸어다님')
        
    def printAddr(self):
        print('주소는' + self.addr)
        
class Chris(Friend):
    def __init__(self,name,addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self): # 오버라이딩
        print(self.addr + ' 동네를 뛰어다님')
        print(self.addr + ' 에 살고있따')
        
john = John('존','역삼동')
john.printName()
john.printAddr()
john.hobby()
print()
chris = Chris('크리스','사직동')
chris.printName()
chris.hobby()


# 추상클래스 : 추상메소드를 가지고 있는 클래스 , 스스로 객체를만들수없다. , 
# 추상클래스를 상속받은 자식클래스는 반드시 추상메소드를 오버라이드 해야한다! 다형성구사하기위해
from abc import *

class TestClass(metaclass = ABCMeta): # 추상 클래스가 됨
    
    @abstractclassmethod
    def abcMethod(self): # 추상 메소드
        pass

    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')
        
#parent = TestClass() # 불가. !

class Child1(TestClass):
    name = ' 난 child1 멤버 변수'

    def abcMethod(self):      # 메소드 오버라이드 강요당함
        print(' 추상 메소드를 오버라이드함 ! 마법에풀림')
        
c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()

print('-------')
class Child2(TestClass):
    def abcMethod(self): # 강요
        print('추상 메소드를 child2에서도 오버라이드 함')
        print('추상 메소드의 위력을 감상중')
        
    def nomalMethod(self):
        print('추상 클래스 내의 일반 메소드는 오버라이드 해도 되고 안 해도 되고 니맘이야~')
        
c2 = Child2()
c2.abcMethod()
c2.nomalMethod()

print('-- 다형성 --')
mbc = c1
mbc.abcMethod()
print()
mbc = c2
mbc.abcMethod()

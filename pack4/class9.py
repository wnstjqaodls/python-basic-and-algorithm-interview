# 메소드 오버라이드를 이용해 다형성 구사

class Parent: # 보무클래스의 역할만 함 . 자식클래스에서 printData 를 오버라이딩해서 사용하시오! 라는 의미가된다
    def printData(self):
        pass
    
    
class Child1(Parent):
    def printData(self):
        print('child1에서 override')
        
        
        
class Child2(Parent):
    def printData(self):
        print('child2에서 재정의')
        print('부모 메소드와 동일한 이름을 가지나 기능은 다르다')
        
    def aa(self):
        print('child2 고유 메소드')
        

c1 = Child1()
c1.printData()
print()
c2 = Child2()
c2.printData()

print('\n다형성 : 동일한 명령문이나 기능은 다름----')
#par = Parent()     # 주석처리를해도 실행이된다

par = c1       # 자식의 객체를 치환! 할 때 자바처럼 꼭 부모 객체변수에 지환할 필요없다. 일반변수에 치환하면된다.
par.printData()    # 메서드 이름은같으나...

print()

par = c2
par.printData()    #이름은같으나 .. 하는일은 다르다.


plist = [c1,c2]
for i in plist:
    i.printData()
    print()
    

    
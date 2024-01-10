# 클래스 : 자원의 재활용. 다형성을 구사
# 자바와 차이 : 생성자의 모양이 다름, 메소드 오버로딩 없다. 다중상속이 가능. 멤버는 public. 모듈의 멤버중 하나
print('뭔가를 하다가 클래스를 선언')

class TestClass:   # 원형 클래스로 메모리를 확보(기억공간을 갖음)
    aa = 1  # 멤버변수, 멤버 필드, 클래스 변수
    
    def __init__(self):
        print('생성자')
        
    def __del__(self):
        print('소멸자')
        
    def printMsg(self):
        print('메소드')
        name = '홍길동'   # 메소드 내에서만 유효한 지역변수
        print(name)  
        print(self.aa)  # 클래스의 멤버는 self.~

print(TestClass.aa)
#TestClass.printMsg(self)  # X    self에 값을 매칭을 못함

print()
test = TestClass()  # 생성자를 호출하고 TestClass 타입의 객체 생성
print(test.aa)
test.printMsg()  # Bound method call
TestClass.printMsg(test)  # UnBound method call

print()
print('클래스 타임은 ', isinstance(test, TestClass))

print()
print(type(1))  # <class 'int'>   Python 제작자가 만든 타입
print(type('abc'))  # <class 'str'>
print(type(test))  # <class '__main__.TestClass'>  새로운 타입이 만들어짐
print(id(TestClass))
print(id(test))

del test  # 객체변수 삭제


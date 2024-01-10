# 상속
class Person:
    Say = '난 사람이야~'
    nai = 20
    __abc = 'good'    # private 멤버변수
    
    def __init__(self,nai):
        print('Person 생성자 호출')
        self.nai = nai
        
    def printInfo(self):
        print('나이:{} ,이야기:{}'.format(self.nai,self.Say))
        
        
    def hello(self):
        print('안녕')
        print(self.__abc)
        
print(Person.Say,Person.nai)
# Person.printInfo() 값이없어서 안됨
P = Person('22')
print(P.Say,P.nai)
#P.printInfo()
P.hello()


print('***'*10)
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    
    def __init__(self):
        print('employee 생성자')
        
    def printInfo(self):      #메소드 오버라이드
        print('employee 클래스에서 오버라이드한 프린트인포')
        
    def e_printInfo(self):
        self.printInfo()
        super().printInfo()    # 부모꺼 소환 부모메소드를 호출
        
        
e = Employee()
print(e.say,e.nai,e.subject)
e.printInfo()
e.e_printInfo()

print('~~'*10)
class Worker(Person):
    def __init__(self,nai):
        print('worker 생성자')
        super().__init__(nai)
        
    def w_printInfo(self):
        self.printInfo()
        
    
w = Worker('25')
print(w.Say,w.nai)
w.w_printInfo()


print('-----------------')
class Programer(Worker):
    def __init__(self,nai):
        print('programer 생성자')
        Worker.__init__(self, nai) # 부모클래스 생성자호출 . unbound method call 클래스 이름으로호출했음
        
    def p_printInfo(self):
        self.printInfo()
        
        
pr = Programer('33')
print(pr.Say,pr.nai)
pr.p_printInfo()


print('-----------------------------')
a = 10; print(type(a))
print(type(pr))
print(type(w))
print(Programer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)
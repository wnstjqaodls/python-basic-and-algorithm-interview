from abc import *

class Employee(metaclass=ABCMeta):

    def __init__(self,irum,nai):
        self.irum = irum
        self.nai = nai
        
    @abstractclassmethod
    def pay(self):
        pass
    
    @abstractclassmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print('이름은',self.irum,'나이는',self.nai,end = ' ')
        
    
    
class Temporary(Employee):
    def __init__(self,irum,nai,ilsu,ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        
    def pay(self):
        return self.ilsu * self.ildang
    
    def data_print(self):
        self.irumnai_print()
        print(', 월급' + str(self.pay()))
        
class Regular(Employee):
    def __init__(self,irum,nai,salary):
        Employee.__init__(self, irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary
    
    def data_print(self):
        self.irumnai_print()
        print(', 급여:'+ str(self.pay()))


class Salesman(Employee):
    def __init__(self,irum,nai,salary,sales,commission):
        Employee.___init__(self,irum,nai,salary)
        self.sales = sales
        self.commission = commission
    
    def pay(self):
        return super().pay() + (self.sales * self.commission)
        
    def data_print(self):
        self.irumnai_print()
        print(', 수령액 :' + str(round(self.pay())))
        
        
t1 = Temporary('영권',25,20,150000)
t1.data_print()

r1 = Regular('현욱',27,3500000)
r1.data_print()

s1 = Salesman('영업왕',29,120000,5000000,0.25)
s1.data_print()


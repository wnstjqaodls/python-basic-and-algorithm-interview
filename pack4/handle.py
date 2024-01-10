# 부품을 별도의 클래스를 작성
# 핸들 
class PohanmHandle:
    quantity = 0 #회전량 이라고 정의하자
    
    def leftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def rightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    
    
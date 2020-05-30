# 실습과제 5-6(Calculator class)
## 4칙연산이 가능한 클래스
### a = FourCal()
### a.setdata(4,2)
### a.add()...

class FourCal:
    def __init__(self):
        pass

    def setdata(self, num1, num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2
    
    def mul(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2

cal = FourCal()
cal.setdata(4, 2)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
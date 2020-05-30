# 실습과제 5-10(Upgrade Calculator)

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value+=val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value-=val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 실습과제 5-11(MaxLimitCalculator)
## 객체변수 value가 100미만이 되도록 제한하는 클래스

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value+=val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value+=val
        if self.value>=100:
            self.value = 99

mlc = MaxLimitCalculator()
mlc.add(50)
mlc.add(60)

print(mlc.value)

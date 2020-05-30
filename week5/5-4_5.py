# 실습과제 5-4
## Coordinate 클래스 정의
## distance()메서드 정의 하나의 인스턴스를 매개변수로 전달받아 거리 계산
## 인스턴스 새로 생성하여 메서드 테스트

# 실습과제 5-5
## Coordinate 클래스의 인스턴스화 과정에서 x와 y초기화할 수 있게
## 초기값 전달되지 않은 경우 기본값 0

import math

def square(x):
    """전달 받은 수의 제곱을 반환한다."""
    return x*x

class Coordinate:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def distance(self, other):
        return math.sqrt(square(self.x-other.x)+square(self.y-other.y))

p1 = Coordinate()
p2 = Coordinate(3, 4)

print(p1.distance(p2))

import math

# 실습과제 5-1(Coordinate class)
## 좌표를 나타내는 클래스 coordinate를 정의
## 클래스 속성으로 x와 y를 정의(초기 값: 0)


class Coordinate:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

# 실습과제 5-2(Coordinate class)
## Coordinate()클래스의 인스턴스 두 개 생성,
## point_1(x=-1, y=2)/ point_2(x=2, y=3)

point_1 = Coordinate(-1, 2)
point_2 = Coordinate(2, 3)

# 실습과제 5-3(Coordinate class)
## 좌표 인스턴스의 거리 계산하기

def square(x):
    """전달 받은 수의 제곱을 반환한다."""
    return x*x

def distance(point_a, point_b):
    """두 점 사이의 거리를 계산해 반환한다.(피타고라스의 정리)"""
    return math.sqrt(square(point_a.x-point_b.x)+square(point_a.y-point_b.y))

print(distance(point_1, point_2))

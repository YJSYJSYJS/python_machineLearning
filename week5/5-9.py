# 실습과제 5-9(도형클래스 정의하기 2)

import math

def square(x):
    return x*x

class Coordinate:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def distance(self, other):
        return math.sqrt(square(self.x-other.x)+square(self.y-other.y))

class Shape:
    def describe(self):
        print("이 도형은 {} 개의 변을 갖고 있습니다.".format(self._sides_))

class Triangle(Shape, Coordinate):
    _sides_ = 3
    p1 = Coordinate()
    p2 = Coordinate()
    p3 = Coordinate()

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def circumference(self):
        return self.p1.distance(self.p2)+self.p2.distance(self.p3)+self.p3.distance(self.p1)

class Rectangle(Shape, Coordinate):
    _sides_ = 4
    p1 = Coordinate()
    p2 = Coordinate()
    p3 = Coordinate()
    p4 = Coordinate()
    
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def circumference(self):
        return self.p1.distance(self.p2)+self.p2.distance(self.p3)+self.p3.distance(self.p4)+self.p4.distance(self.p1)

tri = Triangle(Coordinate(0,0),Coordinate(3,0),Coordinate(0,4))

rect = Rectangle(Coordinate(0, 0), Coordinate(2, 0), Coordinate(2, 2), Coordinate(0, 2))

shapes = [tri, rect]

for s in shapes:
    s.describe()
    print('둘레: ', s.circumference())

# 실습과제 5-8(도형클래스 정의하기)
## 클래스: Shape(도형), Triangle(삼각형), Rectangle(사각형)

class Shape:
    def describe(self):
        print("이 도형은 {} 개의 변을 갖고 있습니다.".format(self._sides_))

class Triangle(Shape):
    _sides_ = 3

class Rectangle(Shape):
    _sides_ = 4

tri = Triangle()
rect = Rectangle()

shapes=[tri, rect]
for s in shapes:
    s.describe()
    
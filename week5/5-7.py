# 실습과제 5-7(직사각기둥)
## 직사각형을 밑면으로 갖는 사각 기둥의 부피를 계산하기 위한 클래스
## 속성: a(밑면 가로 길이), b(밑면 세로 길이), h(높이)
## 메서드: volume(부피 계산), surface(겉넓이 계산)
## 가로, 세로, 높이를 몇 가지 예로 부피와 겉넓이를 계산해보아라.

class RectCol:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    
    def volume(self):
        return self.a*self.b*self.h
    
    def surface(self):
        return 2*(self.a*self.b + self.h*(self.a + self.b))

rc1 = RectCol(2, 2, 4)

print(rc1.volume())
print(rc1.surface())
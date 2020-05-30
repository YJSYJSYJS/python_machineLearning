# 실습과제 5-14(주사위 클래스)
## 객체마다 면의 수(비공개 인스턴스 속성)가 다르다.
## 윗 면(랜덤)을 비공개 인스턴스 속성으로 정의
## 주사위 인스턴스는 하나의 인자(면의 수)를 전달하여 생성
## 인스턴스의 현재 윗면을 반환하는 top() 메서드 정의
## 인스턴스의 윗면을 새 임의의 값으로 설정하고 반환하는 role()메서드 정의

import random

class Dice:

    _t_side = 0

    def __init__(self, sides):
        self.sides = sides        

    def top(self):
        if self._t_side==0:
            self._t_side = random.randint(1, self.sides)    
        return self._t_side

    def roll(self):
        self._t_side = random.randint(1, self.sides)
        return self._t_side

dice_4 = Dice(4)
print('사면체 주사위 테스트 ----')
print('처음 나온 면: ', dice_4.top())
print('다시 굴리기: ', dice_4.roll())
print('다시 굴리기: ', dice_4.roll())

dice_100 = Dice(100)
print('백면체 주사위 테스트 ----')
print('처음 나온 면: ', dice_100.top())
print('다시 굴리기: ', dice_100.roll())
print('다시 굴리기: ', dice_100.roll())

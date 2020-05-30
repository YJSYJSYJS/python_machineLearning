# 실습과제 5-15(음식 클래스)
## 앞의 음식 클래스 Food에 크기 비교 연산 추가
## 클 수록 맛이 좋다, 같으면 칼로리가 더 적은 것이 더 큰 것이다.
## 맛 칼로리 둘다 같으면 음식의 크기가 같다.

class Food:
    """음식을 나타내는 클래스"""
    def __init__(self, taste, calorie):
        """인스턴스를 초기화한다."""
        self._taste = taste
        self._calorie = calorie

    def __str__(self):
        """이 음식을 표현하는 문자열 반환"""
        return str(self._taste) + '만큼 맛있고,' + str(self._calorie) + '만큼 든든한 음식'

    def __add__(self, other):
        """이 음식(self)과 다른 음식(other)을 더한 새 음식 반환"""
        taste = self._taste + other._taste
        calorie = self._calorie + other._calorie
        return Food(taste, calorie)
    
    def __lt__(self, other):
        """self<other?"""
        if self._taste<other._taste:
            return True
        elif self._taste==other._taste:
            if self._calorie>other._calorie:
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        """self>=other?"""
        if self._taste>=other._taste:
            return True
        elif self._taste==other._taste:
            if self._calorie < other._calorie:
                return True
        else:
            return False 

    def __eq__(self, other):
        """self==other?"""
        if self._taste==other._taste and self._calorie==other._calorie:
            return True
        else:
            return False

strawberry = Food(9, 32)
potato = Food(6, 55)
sweet_potato = Food(12, 131)
pizza = Food(13, 266)
print('딸기 < 감자: ', strawberry < potato)
print('감자 + 감자 < 고구마: ', potato + potato < sweet_potato)
print('피자 >= 딸기: ', pizza >= strawberry)
print('피자 >= 피자: ', pizza >= pizza)
print('감자 + 딸기 < 피자: ', potato + strawberry < pizza)
print('딸기 == 딸기: ', potato == potato)

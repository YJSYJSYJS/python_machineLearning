# 해당 숫자의 구구단 한 줄로 출력


def muls(num):
    for i in range(1,10):
        print(num*i, end=' ')

number = int(input("구구단 출력할 숫자를 입력: "))

muls(number)
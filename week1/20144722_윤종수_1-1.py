# 주어진 자연수가 홀수인지 짝수인지 판별할 수 있는 방법에 대해서 말해보자.

number = int(input("자연수를 입력하세요"))
print(type(number))
if number%2==0:
    print("{} is even number".format(number))
else:
    print("{} is odd number".format(number))
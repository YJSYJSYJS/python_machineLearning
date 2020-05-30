# 콜라츠 추측: 임의의 자연수가 다음 조작을 거쳐 항상 1이 된다
# 짝수 -> 2로 나눈다.
# 홀수 -> 3을 곱하고 1을 더한다.
# 1이면 조작을 멈추고, 1이 아니면 첫번째 단계로 돌아간다.
# 이 조작을 통해서 생성되는 수열 우박수
# 임의의 자연수 입력받아 우박수 출력

x = int(input('자연수를 입력하세요: '))
temp = x

def hail(num: int) -> int:
    if num%2==0:
        num = num/2
    else:
        num = num*3 + 1
    return num

print(temp)

while temp != 1:
    temp = hail(temp)
    print(int(temp))


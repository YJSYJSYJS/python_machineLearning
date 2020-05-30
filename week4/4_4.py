# 개수 미정의 입력받은 숫자의 총합을 출력하는 함수
nums=[]
while True:
    num= int(input('숫자 입력:'))
    if num==0:
        break
    nums.append(num)

def sum_of(args):
    return(sum(args))

print(sum_of(nums))
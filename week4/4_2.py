 # 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자(입력의 수는 정해져 있지 않다.)
nums=[]
while True:
    num = int(input("숫자 입력:"))
    if num==0:
        break
    nums.append(num)

def avg(args):
    return sum(args)/len(args)

print(avg(nums))
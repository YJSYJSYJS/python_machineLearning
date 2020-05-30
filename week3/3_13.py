# 입력받은 수가 prime number인지 판별하는 프로그램을 생각
# prime number(소수): 약수가 1과 자기자신뿐인 2이상의 자연수
# for문과 while문 이용 각각 작성
# 프로그램을 이용하여 1부터 100까지 소수의 합

num = int(input("input number: "))

def is_prime(num):
    """
    입력받은 수가 소수인지 1부터 num-1까지 나눠떨어질때까지 순회
    나눠떨어지면 return True
    반복문이 종료되면 return False
    """
    for i in range(2,num):
        if num%i==0:
            return False
    return True

pr_li = [0, 0] + [1] * 99
sum=0
for i in range(2, 101):
    if is_prime(i):
        sum+=i
        for k in range(2, 101):
            if i*k>100:
                break
            pr_li[i*k]=0

print(sum)

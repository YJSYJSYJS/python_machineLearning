# 완전수: 자기 자신을 제외한 양의 약수를 더했을 때 자기 자신이 되는 양의 정수
# 최초 네개의 완전수: 6, 28, 496, 8128

def is_com(num: int) -> bool:
    """
        입력 받은 숫자가 완전수이면 True
        아니면 False
        나누어 떨어지는 경우 몫을 반복횟수로 갱신하여
        계산비용을 낮추었다.
        약수를 따로 저장하지 않고 바로 sum에다가 더해주었다. 
    """
    sum = 1
    limit = num
    i = 2
    while i<limit:
        if num%i==0:
            sum += i+num//i
            limit = num//i
        i+=1
    if sum == num and num!=1:
        return True
    else:
        return False

for i in range(9999):
    if is_com(i):
        print(i)

print('33550336: ', is_com(33550336))
print('8589869056: ', is_com(8589869056))
print('137438691328: ', is_com(137438691328))

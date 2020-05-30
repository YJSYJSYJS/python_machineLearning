# Happy number

is_happy_list = [0] * 1001

def square_sum(num: int):
    """
    각 자리수를 제곱하여 더한다.
    """
    sum = 0

    while num>=1:
        temp = num%10
        sum += temp**2
        num = num//10 
        
    return sum

def is_happy(num):
    """
    숫자의 각자리 수의 제곱의 합은 한 자리수인 경우 9가지
    두 자리수인 경우 9**2가지
    세 자리수인 경우 9**3가지로 정해져 있으며, 패턴이 있다는 것을 활용!
    happy number로 판단된 경우
    그 과정에서의 제곱합 값들도 모두 happy number이다!
    아닌 경우 그 과정에서의 제곱합 값들은 모두 happy number가 아니다!
    """
    check = square_sum(num) # 일단 제곱합 해본다.
    global is_happy_list # happy 여부가 저장된 리스트를 불러온다.
    temp = list() # true일 경우 temp값을 활용 happy들을 is_happy_list에 갱신할 예정
    while True: # 무한 루프
        if check in temp or is_happy_list[check]==-1: 
            # 제곱합이 제곱합 수열인 temp에 이미 있거나, 예전에 이미 -1일 경우
            temp.append(check)
            temp.append(num)
            for t in temp:
                is_happy_list[t] = -1
            return False
        elif check == 1 or is_happy_list[check] == 1: 
            # 제곱합 1 이거나 is_happy_list에 1로 되어있을 경우
            temp.append(check)
            temp.append(num)
            for t in temp: # temp의 원소들은
                is_happy_list[t] = 1 # 전부 happy인 것으로 is_happy_list에 갱신
            return True
        else: # happy 여부 판단이 안되면
            temp.append(check)
            check = square_sum(check) # 제곱합을 한번더 실행한다.
        if num==7:
            print(check)
            print(temp)

for i in range(1, 1001):
    if i == 7:
        print(7)
    if is_happy_list[i]==0:
        is_happy(i)
    else:
        continue
        
print(is_happy_list)
happy_list = list()

for i, is_h in enumerate(is_happy_list):
    if is_h==1:
        happy_list.append(i)

print(happy_list)

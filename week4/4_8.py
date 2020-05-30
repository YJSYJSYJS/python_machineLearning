# 짝홀판별함수에서 입력이 자연수가 아닌경우를 try except사용

number = input("자연수를 입력하세요 ")

def is_natural_num(in_num):
    """
    입력이 자연수일 때까지 입력받고, 자연수인 경우 리턴한다.
    """
    try:
        num = int(in_num)
        if num<1:
            new_input = input("자연수는 1이상의 정수입니다. 다시 자연수를 입력해주세요")
            return is_natural_num(new_input)
        else:
            return num
    except ValueError:
        print("자연수가 아닌 것을 입력하셨습니다.")
        new_input = input("'자연수'를 입력하세요 ")
        return is_natural_num(new_input)
    
def is_odd(num):
    """
    입력이 홀수인지 아닌지 판별한다.
    """
    if num%2==0:
        return False
    else:
        return True

natural_num = is_natural_num(number)

if is_odd(natural_num):
    print("{}: 홀수".format(natural_num))
else:
    print("{}: 짝수".format(natural_num)) 

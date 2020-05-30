# random 모듈을 임포트하여 1 이상 32 이하인 수 하나를 임의로 생성 후
# 6 번 이하의 시도로 맞추는 게임을 프로그래밍

import random

y = random.randrange(1, 33)

print('What is the number?')
cnt = 0

while True:
    x = int(input())
    if x>y:
        print('smaller than {}.'.format(x))
    elif x==y:
        print('Congrat!')
        break
    else:
        print('bigger than {}.'.format(x))
    cnt +=1
    if cnt==6:
        re = input('Retry? y/n: ')
        if re == 'y':
            cnt = 0
            print('What is the number?')
        elif re == 'n':
            break
    

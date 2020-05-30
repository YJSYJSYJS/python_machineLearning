# 난수 모듈 이용 seed 적절 값으로 고정
# 20개의 숫자를 0에서 10중에서 발생
# 리스트에 저장(loop)
# 리스트 원소들의 평균(모듈, 계산식 모두 인정)
# math 모듈과 loop(->numpy.array 사용)을 이용 오차제곱의 합의 제곱근 계산
# 통계 모듈의 표본표준편차와 비교

import numpy as np
import random
import math
import statistics

random.seed(100)

total = list()

for i in range(20):
    total.append(random.randint(0, 10))

avg = np.mean(total)

print(total)
print(avg)

# 반복문 사용

sum = 0
for i in total:
    sum += (i-avg)**2

sum = sum/19
print(math.sqrt(sum))

# 반복문 대신 넘파이를 사용
def sum_squares_error(y, t):    
    return np.sum((y-t)**2)

error_sum = sum_squares_error(np.array(total), avg)/19

print(math.sqrt(error_sum))

print('통계 모듈: ', statistics.stdev(total), '로 동일')
print()
print('at numpy module ')
print('비편향 표본표준편차: ', np.std(total, ddof=1), '로 동일')
print('편향 표본표준편차: ', np.std(total), '로 차이가 있음')

# 1부터 1000까지의 자연수 중 3의 배수의 합을 구하시오.
sum = 0
for i in range(1000):
    if i%3==0:
        sum+=i
    else:
        i+=2

print('1부터 1000까지 3의 배수의 합: ', sum)    
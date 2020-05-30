# for문을 이용하여 A학급의 평균 점수를 구해보자.
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum=0

for score in A:
    sum+=score

avg=sum/len(A)

print("A학급의 평균점수: ", avg)
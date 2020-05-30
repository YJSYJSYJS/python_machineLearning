# 카이사르 암호
# 평행이동은 양의 정수만, 26으로 나눈 나머지 이용

print(chr(65))

d = int(input('원하는 평행 이동: '))

if d>26:
    d = d%26

m = input('보내고 싶은 메시지: ')

ka = list()

for i in m:
    if ord(i)+d<90:
        ka.append(chr(ord(i)+d))
    else:
        ka.append(chr(ord(i)+d-26))

print(ka)
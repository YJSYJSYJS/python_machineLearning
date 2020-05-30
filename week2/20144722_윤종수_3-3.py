input_str = input('주민등록번호: ')
nums = list(map(int,input_str.replace('-','')))
mul = [2,3,4,5,6,7,8,9,2,3,4,5]
sum = int()
for i in range(12):
    sum += int(nums[i])*mul[i]

ans = 11 - sum%11

if nums[12]==ans:
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')
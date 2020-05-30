# 1에서 100까지 숫자를 리스트에 append할 것, 단 3, 6, 9는 *를 append할 것
result=[]
for i in range(1,101):
    i_str = str(i)
    is_changed=False
    if '3' in i_str:
        i_str = i_str.replace('3', '*')
        is_changed=True
    if '6' in i_str:
        i_str = i_str.replace('6', '*')
        is_changed=True
    if '9' in i_str:
        i_str = i_str.replace('9', '*')
        is_changed=True
    if is_changed:
        result.append(i_str)
    else:
        result.append(i)
print(result)
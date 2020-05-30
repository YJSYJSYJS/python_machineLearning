my_list = ['A', 'b', 'c', 'D']
for m in my_list:
    if m.isupper():
        print(m.lower(), end=' ')
    else:
        print(m.upper(), end=' ')

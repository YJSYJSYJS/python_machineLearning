'''
a = {'A':90, 'B':80}
print(a['C'])
print('KeyError')
'''

# 1
a = {'A': 90, 'B': 80}
b = a.get('C', 70)
print(b)

# 2
try:
    print(a['C'])
except KeyError:
    print(70)
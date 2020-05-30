a = "a:b:c:d"
b = a.replace(':','#')
print(b)

c = a.split(':')
d = '#'.join(c)
print(d)
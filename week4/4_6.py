# fibonacci

fib=[0, 1, 1,]

def fib0(n):
    global fib
    if n>=3:
        for i in range(3,n+1):
            fib.append(fib[i-1]+fib[i-2])
    print(fib[n])

fib0(20)

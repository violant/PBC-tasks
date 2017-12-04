def fib(n):
    s1 = 0
    s0 = 0
    for i in range(2,n-1):
        s0 = s1
        s1 = s0 + s1
        print (s1)


n=6
print fib(n)
def fib(n):
    s0 = 0
    s1 = 1
    if n >= 1:
        print (s0),
    if n >= 2:
        print (s1),
    if n >= 3:
        for i in range(2, n):
            s2 = s0 + s1
            s0 = s1
            s1 = s2
            print (s2),


n = 7
fib(n)
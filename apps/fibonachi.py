def fib(n):
    s0 = 0
    s1 = 1
    fibo = []
    if type(n) is not int:
        return fibo
    if n >= 1:
        fibo.append(s0)
    if n >= 2:
        fibo.append(s1)
    if n >= 3:
        for i in range(2, n):
            s2 = s0 + s1
            s0 = s1
            s1 = s2
            fibo.append(s2)
    return fibo


#n = 10.1
#print(fib(n))
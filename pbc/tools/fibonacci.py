# ./app.py
import argparse
from pbc.func_decorator import decorator


@decorator
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fibonacci sequence")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--number", "-n", action='store', help="Number of Fibonacci sequence", type=int, required=True)
    args = parser.parse_args()
    str_fib = str(fib(args.number)).strip('[]')
    print (str_fib)

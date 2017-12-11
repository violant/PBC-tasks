import argparse
from pbc.tools.fibonacci import fib
from pbc.tools.numbers import pair

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fibonacci sequence or print pairs with sum 10 from list")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--fib", "-f", action='store_true', help="to run fibonachi")
    group.add_argument("--number", "-n", action='store', help="Number of Fibonacci sequence", type=int, required=False)
    group.add_argument("--pairs", "-p", action='store_true', help="to run pairs")
    group.add_argument("--list", "-l", action='store', nargs='+',
                       help="List of int with space delimiter. For example 1 2 3 34 678 ", type=int, required=False)
    args = parser.parse_args()
    if args.fib:
        str_fib = str(fib(args.number)).strip('[]')
        print (str_fib)

    elif args.pairs:
        print (pair(*args.list))

# args.py
import argparse
from pbc.func_decorator import decorator

summ = 10


@decorator
def pair(*list_elem):
    pair_res = set()
    i = 0
    j = 0
    for i in range(list_elem.__len__()):
        for j in range(list_elem.__len__()):
            if (list_elem[i] + list_elem[j] == summ) and (i != j):
                pair_found = min(list_elem[i], list_elem[j]), max(list_elem[i], list_elem[j])
                pair_res.add(pair_found)
    return pair_res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app print pairs with sum 10 from list")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--list", "-l", action='store', nargs='+',
                       help="List of int with space delimiter. For example 1 2 3 34 678 ", type=int, required=True)
    args = parser.parse_args()
    print (pair(*args.list))

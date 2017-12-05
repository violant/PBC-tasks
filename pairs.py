summ = 10


def find_pair(cur, *list_elem):
    for ele in list_elem:
        if ele + cur == summ:
            tup=(ele, cur)
            return min(ele, cur), max(ele, cur)


def pair(list_elem):
    pair_res = set()
    for elem in list_elem:
        pair_res.add(find_pair(elem, *list_elem))
    return pair_res


list_ele = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
print(pair(list_ele))

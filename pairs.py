summ = 10


def find_pair(cur, *list_elem):
    for ele in list_elem:
        if ele + cur == summ:
            return min(ele, cur), max(ele, cur)


def pair(list_elem):
    pair_res = set()
    for elem in list_elem:
        if find_pair(elem, *list_elem) is not None:
            pair_res.add(find_pair(elem, *list_elem))
    return pair_res


list_ele = [17, 4, 5, 6, 5, 4, 9]
print(pair(list_ele))

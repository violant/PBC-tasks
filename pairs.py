summ = 10


def pair(list_elem):
    pair_res = set()
    i=0
    j=0
    for i in range(list_elem.__len__()):
        for j in range(list_elem.__len__()):
            if (list_elem[i] + list_elem[j] == summ) and (i != j):
                pair_found = min(list_elem[i], list_elem[j]), max(list_elem[i], list_elem[j])
                pair_res.add(pair_found)
    return pair_res


#list_ele = [7, 3]
#print(pair(list_ele))

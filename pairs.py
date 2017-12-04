summ = 10


def find_pair(cur, *list_elem):
    for ele in list_elem:
        if ele + cur == summ:
            return (ele, cur)


def pair(list_elem):
    for elem in list_elem:
        print(find_pair(elem, *list_elem))


list_ele = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
pair(list_ele)

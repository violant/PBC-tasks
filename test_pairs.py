from pairs import pair

#test_data
arr1 = [4, 5, 6, 7, 3]
arr2 = [17, 4, 5, 6, 5]
arr3 = [1, 2, 3, 4, 5]
arr4 = []
arr5 = [765]
res1 = set([(3, 7), (4, 6)])
res2 = set([(4, 6), (5, 5)])
empty_set = set([])
res6 = set([(3, 7), (4, 6), (5, 5)])


#list with one 5
def test_1():
    assert pair(arr1) == res1


#list with two 5
def test_2():
    assert pair(arr2) == res2

#list without pairs
def test_3():
    assert pair(arr3) == empty_set

#empty list
def test_4():
    assert pair(arr4) == empty_set

#list with one value
def test_5():
    assert pair(arr5) == empty_set


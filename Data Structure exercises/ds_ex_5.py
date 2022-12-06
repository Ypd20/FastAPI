list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]
list3 = [(i,j) for i, j in zip(list1, list2)]
print(list3)
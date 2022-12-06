l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = list()

odd_elements = l1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = l2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
l3.extend(odd_elements)
l3.extend(even_elements)
print(l3)
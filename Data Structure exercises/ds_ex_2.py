list1 = [54, 44, 27, 79, 91, 41]
print("Original list ", list1)
element = list1.pop(4)
print("List After removing element at index 4:", list1)

list1.insert(2, element)
print("List after Adding element at index 2:", list1)

list1.append(element)
print("List after Adding element at last:",list1)
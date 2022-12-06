def value(a,b):
    print("entered value are",a,b)
    def addition(a,b):
        return a + b
    add = addition(a, b)
    return add + 5

result = value(5, 10)
print("The sum of given value + 5 is",result)



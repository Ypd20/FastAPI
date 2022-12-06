def sum(num):
    if num:
        return num + sum(num - 1)
    else:
        return 0

res = sum(10)
print(res)

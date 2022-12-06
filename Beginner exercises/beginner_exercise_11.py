num = 7536
n=0
while num>0:
    rev = num%10
    num = num - rev
    num = num/10
    print(int(rev),end="")
    n = n + 1   
print(n)

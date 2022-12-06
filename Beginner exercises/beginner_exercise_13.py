for i in range(1, 11):
    print('Multiplication table of:', i)
    count = 1
    
    while count < 11:
        print(i * count, end=' ')
        count = count + 1
    print('\n')
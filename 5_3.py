n = int(input('Введите диапозон: '))

count = 0
for i in range(2, n+1, 2):
    if count < 5:
        print (i, end=" ")
        count +=1
    else:
        print()
        print(i, end=" ")
        count = 1


list_1 = list(input('введите список чисел: '))
print(list_1)
n = int(input("Введите число: "))
if n < 0 or n > len(list_1):
    print('неверное число')
else:
    var = list_1[0:-n]
    var_1 = list_1[len(list_1)-n: ]
    print(var)
    var_1.extend(var)
    print(var_1)





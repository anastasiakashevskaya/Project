#заполнить список стеменями числа 2(от 1 до n)
number = int(input('Введите число: '))
two = []
while number >= 0:
    two.append(2**number)
    number -= 1
    if number == 0:
        break
        two.reverse()
print(two)

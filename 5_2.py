number_1 = int(input("введите число 1: "))
sign = input("введите действие (+, -, *, /): ")
number_2 = int(input("введите число 2: "))
if sign == "+":
    print(number_1, '+', number_2, '=', number_1+number_2)
elif sign == '-':
    print(number_1, '-', number_2, '=', number_1-number_2)
elif sign == '*':
    print(number_1, '*', number_2, '=', number_2*number_1)
elif sign == '/':
    if number_2 !=0:
        print(number_1, "/", number_2, '=', number_1/number_2)
    else:
        print('на ноль делить нельзя!')


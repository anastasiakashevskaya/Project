number1 = input('Введите первое число: ')
number1 = float(number1)
number2 = input('Введите второе число: ')
number2 = float(number2)
number3 = input('Введите третье число: ')
number3 = float(number3)
pos=0
if number1 > 0:
    pos=pos+1
if number2>0:
    pos=pos+1
if number3>0:
    pos=pos+1
print('Количество положительных чисел: ', pos)
neg=0
if number1 < 0:
    neg=neg+1
if number2<0:
    neg=neg+1
if number3<0:
    neg=neg+1
print('Количество отрицательных чисел: ', neg)






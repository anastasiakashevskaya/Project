name = input('Введите Ваше имя: ')
age = input('Введите Ваш возраст: ')
age=int(age)
city = input('Введите Ваш город: ')
welcome = "Приветствуем Вас, {}, {}, из города {}.".format(name, age, city)
print(welcome)
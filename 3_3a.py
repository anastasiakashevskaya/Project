name = input('Введите Ваше имя: ')
age = input('Введите Ваш возраст: ')
age=int(age)
city = input('Введите Ваш город: ')
welcome = "Приветствуем Вас, %(name)s, %(age)d, из города %(city)s" % {"name": name, "age": age, "city": city}
print(welcome)


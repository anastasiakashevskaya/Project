number = int(input("Введите количество: "))
users = {
    i: {
        "name": input("name: "),
        "email": input("email: ")
    } for i in range(number)
}

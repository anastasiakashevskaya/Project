n = int(input('количество: '))
m = int(input("кратное: "))
k = int(input ('не больше: '))
i = k
count = 0
while count < n:
    if not i % m:
        count += 1
        print(i)
    i += 1



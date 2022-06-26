n = int(input('количество: '))
m = int(input("кратное: "))
k = int(input ('не больше: '))
counter = 0
for i in range(1, k):
    if i % m == 0:
        counter +=1
        print(i)



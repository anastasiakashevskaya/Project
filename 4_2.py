# словарь для подсчитывания количества вхождений каждой буквы
text = input("Введите текст: ")
dictionary = {symbol: text.count(symbol) for symbol in text}
print(dictionary)
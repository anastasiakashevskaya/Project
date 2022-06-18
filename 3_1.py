text = 'London is the capital of Great Britain'
text = text.replace(" ", "-")
print(text)

text2 = 'London is the capital of Great Britain'
text2 = text2.split(' ')
text2 = '-'.join(text2)
print(text2)
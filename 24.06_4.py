my_str = input('Введите предложение: ')
a = my_str.split(' ')
for i, b in enumerate(a, 1):
    if len(b) > 10:
        b = b[0:10]
    print(f"{i}. {b}")
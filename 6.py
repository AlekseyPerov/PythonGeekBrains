a = float(input('Введите значение 1: '))
b = float(input('Введите значение 2: '))
c = 1
if a > b:
    print(c)
while a < b:
     a = a + a/10
     c = c + 1
print(c)
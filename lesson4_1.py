from sys import argv
name, a, b, c = argv
try:
    if float(a) < 0 or float(b) < 0 or float(c) < 0:
        print('Отрицательное значение невозможно!')
    else:
        salary=float(a)*float(b)+float(c)
        print(f"Зарплата: {salary}")
except ValueError:
    print('Только числовые значения!')
# вызывал через терминал или cmd
# python lesson4_1.py 2 3 4
# сам lesson4_1.py положил в папку pythonProject

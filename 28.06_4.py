def my_f(x, y):
    if x > 0 and y < 0:
        z = 1 / x ** abs(y)
        print(f"Результат: {z}")
    else:
        print('Число X должно быть положительным а Y отрицательным!')

my_f(int(input('Введите X: ')), int(input('Введите У: ')))

"""def my_f(x, y):
    z = pow(x, y)
    print(f"Результат: {z}")


my_f(int(input()), int(input()))"""
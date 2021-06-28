def my_f(arg_1, arg_2):
    try:
        arg = arg_1 / arg_2
        print(f"Результат деления: {arg}")
        return arg
    except ZeroDivisionError:
        print('На 0 делить нельзя.')

my_f(arg_1=int(input('Введите делимое: ')), arg_2=int(input('Введите делитель: ')))
def my_f(arg_1, arg_2, arg_3):
    if arg_1 >= arg_2 and arg_3 >= arg_2:
        return arg_1 + arg_3
    elif arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_2 >= arg_1 and arg_3 >= arg_1:
        return arg_2 + arg_3
print(f'Результат: {my_f(int(input("Укажите первый аргумент:  ")), int(input("Укажите второй аргумент:  ")), int(input("Укажите третий аргумент:  ")))}')
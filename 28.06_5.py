def my_f ():
    sum = 0
    exit = False
    while exit == False:
        number = input('Введите число или Q для выхода: ').split()
        tmp = 0
        for el in range(len(number)):
            if number[el] == 'Q' or number[el] == 'q':
                exit = True
                break
            else:
                tmp = tmp + int(number[el])
        sum = sum + tmp
        print(f'Текущая сумма:{sum}')
    print(f'Итоговая сумма: {sum}')


my_f()
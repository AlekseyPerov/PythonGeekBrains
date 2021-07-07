def summary():
    try:
        with open('file_2.txt', 'w+') as new_file:
            line = input('Введите цифры через пробел: \n')
            new_file.writelines(line)
            my_numb = line.split()
        print(sum(map(int, my_numb)))
    except ValueError:
        print('Вводите числа а не буквы.')
summary()
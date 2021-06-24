my_list = ['зима', 'весна', 'лето', 'осень']
my_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input('Введите месяц в виде числа: '))
while month >= 13:
    print('Такого месяца не существует')
    break
if month == 12 or month == 1 or month == 2:
    print('Сейчас', my_list[0])
    print('Сейчас', my_dict.get(1))
elif month == 3 or month == 3 or month == 5:
    print('Сейчас', my_list[1])
    print('Сейчас', my_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print('Сейчас', my_list[2])
    print('Сейчас', my_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print('Сейчас', my_list[3])
    print('Сейчас', my_dict.get(4))
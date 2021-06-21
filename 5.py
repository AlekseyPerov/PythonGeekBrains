vir = int(input('Укажите значение выручки '))
izd = int(input('Укажите значение издержек '))
if vir >= izd:
    profit = vir - izd
    rent = vir / izd
    print ('Ваша выручка ', profit)
    sotr = int(input('Кол-во сотрудников: '))
    profs = profit / sotr
    print (profs, 'на одного сотрудника')
else:
    print ('Выручки нет')
#
msec = int(input('Введите время в секундах - '))
hours = msec // 3600
ostatok = msec % 3600
minutes = ostatok // 60
seconds = ostatok % 60
print (f'{hours}:{minutes}:{seconds}')
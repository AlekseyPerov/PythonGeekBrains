def my_f(name, surname, date, city, email, phone):
    try:
        a = int(date)
        b = int(phone)
        print(name, surname, date, city, email, phone)
    except:
        print('Используйте цифры!')

my_f(name=input('Введите Имя: '), surname=input('Введите Фамилия: '), date=input('Введите год рождения: '), city=input('Укажите город рождения: '), email=input('Укажите емэил: '), phone=input('Укажите телефон: '))
my_data = int(input('Введите данные: '))
my_list = []
a = 0
b = 0
while a < my_data:
    my_list.append(input('Введите данные: '))
    a = a + 1
for i in range(int(len(my_list)/2)):
    my_list[b], my_list[b + 1] = my_list [b + 1], my_list[b]
    b = b + 2
    print(my_list)
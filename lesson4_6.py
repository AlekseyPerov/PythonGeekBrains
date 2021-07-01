from itertools import count, islice
for num in islice(count(int(input('Введите стартовое число: '))), 10):
  print (num)

"""from itertools import cycle, islice
my_list = [1, 2, 3, 4, 5, 'END']
new_list = cycle(my_list)
for num in islice((new_list), 100):
    print(num)"""
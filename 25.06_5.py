my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
for i in range(len(my_list)):
    if my_list[i] == num:
        my_list.insert(i + 1, num)
        break
    elif my_list[0] < num:
        my_list.insert(0, num)
    elif my_list[-1] > num:
        my_list.append(num)
    elif my_list[i] > num and my_list[i + 1] < num:
            my_list.insert(i + 1, num)
print(f"Рейтинг {my_list}")
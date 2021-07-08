with open(r"C:\Users\Perov Alexey\Documents\Python\Lesson 5\text_4.txt", "r+", encoding="utf-8") as my_file:
    rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_file = []
    for i in my_file:
        i = i.split(' ', 1)
        new_file = [line.strip() for line in new_file]
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)
    with open('text_4_new.txt', 'w', encoding="utf-8") as my_file_2:
        my_file_2.writelines(new_file)
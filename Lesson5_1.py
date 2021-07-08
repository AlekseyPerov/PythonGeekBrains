"""my_file = open("file_1.txt", "a", encoding="utf-8")
my_file.write(input('Введите текст \n'))
my_file.close()"""

with open("file_1.txt", "a", encoding="utf-8") as my_file:
    my_file.write(input('Введите текст \n'))
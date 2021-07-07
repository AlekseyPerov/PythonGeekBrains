lines = 0
with open(r"C:\Users\Perov Alexey\Documents\Python\Lesson 5\file_1.txt", "r", encoding="utf-8") as my_file:
    for i in my_file:
        lines +=1
        print(r"Строки: ", lines)
        words = len(i.split())
        print(r"Слова: ", words)
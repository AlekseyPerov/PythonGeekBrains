with open(r"C:\Users\Perov Alexey\Documents\Python\Lesson 5\text_3.txt", "r", encoding="utf-8") as my_file:
    poor = []
    rich = []
    sal = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
            sal.append(i[1])
        else:
            rich.append(i[0])
print(f"Меньше 20000 получают: {poor}, Больше 20000 получают: {rich}, Средний оклад: {sum(map(float, sal)) / len(sal)}")
list = {}
with open('text_6.txt', 'r') as my_file:
        for line in my_file.readlines():
            data = line.replace('(', ' ').split()
            list[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
        print(list)
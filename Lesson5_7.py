from json import dump

with open('text_7.txt', 'r', encoding='utf-8') as r_file:
    with open('text_77.json', 'w', encoding='utf-8') as w_file:
        dictionary = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in r_file}
        av_list = []
        for i in dictionary.values():
            if i > 0:
                av_list.append(i)
        dump([dictionary, {"Средняя прибыль: ": sum(av_list) / len(av_list)}], w_file, ensure_ascii=False,  indent=4)
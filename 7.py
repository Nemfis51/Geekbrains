import json

with open('task7.json', 'w', encoding='utf-8') as my_file:
    with open('for_task7.txt', encoding='utf-8') as qwe:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in qwe}
        result = [profit, {'Средняя прибыль': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                    len([int(i) for i in profit.values() if int(i) >0]))}]
    json.dump(result, my_file, ensure_ascii=False)
pay = {}
with open('for_task3.txt', 'r', encoding='utf-8') as t:
    for line in t:
        pay[line.split()[0]] = float(line.split()[1])
    print('Оклад менее 20000 имеет:')
    for name, qwe in pay.items():
        if qwe < 20000:
            print(name)
    print(f'Средняя величиа дохода {round(sum(pay.values()) / len(pay),2)}')
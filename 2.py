with open('for_task2.txt', 'r', encoding='utf-8') as t:
    print(f'Количество строк в файле - {len(t.readlines())}')
    t.seek(0)
    for i, value in enumerate(t.readlines(), 1):
        print(f'В {i}-ой строке {len(value.split())} слов')
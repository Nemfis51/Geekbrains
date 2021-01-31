import random
with open('for_task5.txt', 'w+', encoding='utf-8') as my_file:
    my_file.write(' '.join([str(random.randint(1, 10)) for qwe in range(10)]))
    my_file.seek(0)
    print(f'Сумма чисел в файле равна: {sum(map(int, my_file.readline().split()))}')








    # l = (my_file.readline().split())
    # print(l)
    # m = sum(map(int, l))
    # print(m)
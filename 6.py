# a

from itertools import count, cycle

for qwe in count(int(input('Введите стартовое число: '))):
    print(qwe)
    if input('Для продолжения пробел, выход "q"') == 'q':
        break


# b

for qwe in cycle(input('Введите элементы через пробел: ').split()):
    print(qwe)
    if input('Для продолжения пробел, выход "q"') == 'q':
         break

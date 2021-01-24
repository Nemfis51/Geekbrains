
def fact(x):
    num = 1
    if x == 0:
        yield '1'
    for i in range(1, x + 1):
        num *= i
        yield num

for el in fact(int(input('Введите число для вычисления: '))):
    print(el)
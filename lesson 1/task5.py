profit = float(input('Введите общую выручку фирмы '))
expenses = float(input("Введите сумму издержек фирмы "))
if profit > expenses:
    print(f'Фирма отработала с прибылью. Рентабельность составила {profit / expenses:.2f}')
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f'прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}')
elif profit == expenses:
    print('Фирма отработала в ноль')
else:
    print('Фирма отработала в убыток')
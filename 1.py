from sys import argv

def payment():
    time, rate, bonus = map(float, argv[1:])
    return(f'Рассчетная сумма - {time * rate + bonus}')

print(payment())

#как лучше выводить первым способом или вот так ?
# def payment():
#     time, rate, bonus = map(float, argv[1:])
#     print(f'Рассчетная сумма - {time * rate + bonus}')
#
# payment()
distance = int(input('Введите результа первого дня в км '))
target = int(input('Введите целевой результат в км '))
days = 1
while target - distance > 0:
        distance = distance + distance * 0.1
        days += 1
print(f'На {days}-й день')
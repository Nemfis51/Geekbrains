
with open('for_task6.txt', 'r', encoding='utf-8') as my_file:
    text = my_file.readlines()
    for qwe in text:
        digits = ''.join((i if i in '1234567890' else ' ') for i in qwe)
        split_digits = [int(i) for i in digits.split()]
        print(f'{qwe.split()[0]} {sum(split_digits)}')
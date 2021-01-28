test_file = open('test.txt', 'w', encoding='utf-8')
while True:
    line = input(f'Введите текст: ')
    if line == '':
        break
    test_file.write(f'{line}\n')
test_file.close()

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('for_task4_out.txt', 'w', encoding='utf-8') as out_file:
    with open('for_task4_in.txt', 'r', encoding='utf-8') as in_file:
        out_file.writelines(line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in in_file)

list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list[num] for num in range(1, len(list)) if list[num] > list[num - 1]]
print(new_list)

# Немного не понял почему след запись
new_set = {list[num] for num in range(1, len(list)) if list[num] > list[num - 1]}
print(new_set)
# выводит множество в порядке увеличения


from functools import reduce

print(reduce(lambda prev_el, el: prev_el * el, [qwe for qwe in range(100, 1001, 2)]))
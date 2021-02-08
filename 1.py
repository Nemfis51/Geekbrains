class Matrix:
    def __init__(self, input):
        self.input = input

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Ошибка размерности матриц'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Ошибка размерности матриц'
        return answer


matrix_1 = Matrix([[1, 3], [5, 7], [9, 11], [13, 15]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)
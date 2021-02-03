class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


pos = Position('Ivan', 'Ivanov', 'middle', 150000, 50000)
print(pos.get_full_name())
print(pos.get_total_income())
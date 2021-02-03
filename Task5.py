class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f' {self.title} рисует')


class Pencil(Stationery):
    def draw(self):
        print(f' {self.title} рисует')


class Handle(Stationery):
    def draw(self):
        print(f' {self.title} рисует')


pen = Pen('Parker')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()
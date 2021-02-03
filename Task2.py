class Road:
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht
    def get_gross(self):
        return f'{self._lenght}м * {self._widht}м * 25кг * 5см = {(self._lenght * self._widht * 25 * 5) / 1000} тонн'
road = Road(5000, 20)
print(road.get_gross())
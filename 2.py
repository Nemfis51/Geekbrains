from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def calculate(self):
        pass

    def __add__(self, other):
        return self.calculate + other.calculate


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)


coat = Coat(40)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)
print(coat + suit)
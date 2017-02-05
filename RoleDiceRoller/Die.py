import random


class Die:
    sides = None
    name = None

    def __init__(self, sides, name=None):
        self.sides = sides
        self.name = name

    def get_sides(self):
        return self.sides

    def roll(self):
        return random.randint(1, self.sides)

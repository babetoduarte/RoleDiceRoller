from RoleDiceRoller.Die import Die


class DiceBag:
    diceList = []

    def find_dice(self, sides):
        for die in self.diceList:
            if die.get_sides() == sides:
                return die

    def die_in_bag(self, sides):
        for die in self.diceList:
            if die.get_sides() == sides:
                return True
        else:
            return False

    def add_die(self, sides, name=None):
        if not self.die_in_bag(sides) == True:
            die = Die(sides, name)
            self.diceList.append(die)

    def remove_die(self, sides):
        if self.die_in_bag(sides):
            self.diceList = [die for die in self.diceList if die.get_sides() != sides]

    def roll_dice(self, ammount, sides):
        result = []
        if self.die_in_bag(sides):
            rolling = self.find_dice(sides)
            for i in range(ammount):
                result.append(rolling.roll())
        return result

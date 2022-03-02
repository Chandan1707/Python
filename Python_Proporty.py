class Student:
    def __init__(self, name, roll):
        self.roll = roll
        self.name = name

    @property
    def name(self):
        return self._name

    @property
    def roll(self):
        return self._roll

    @name.setter
    def name(self, name):
        self._name = name

    @roll.setter
    def roll(self, roll):
        self._roll = roll


s1 = Student('tanu', 39)
print(s1.roll)
print(s1.name)

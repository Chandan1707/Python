class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if temperature < -273.15:
            print('not possible')
            raise ValueError
        self._temperature = temperature

    def to_fahrenheit(self):
        return (9/5 * self.temperature) + 32
    # temperature = property(get_temperature, set_temperature)


t1 = Celsius(37)
print(t1.temperature)
print(t1.temperature)
print(t1.to_fahrenheit())

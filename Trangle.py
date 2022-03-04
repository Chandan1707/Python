
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    def area(self):
        s = 0.5 * (self.a + self.b + self.c)
        result = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return result

    def perimeter(self):
        result = self.a + self.b + self.c
        return result


t1 = Triangle(3, 4, 5)
print('Area :', t1.area())
print('Perimeter :', t1.perimeter())

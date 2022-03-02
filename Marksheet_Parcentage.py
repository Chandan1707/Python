class MarksheetPercentage:
    def __init__(self, num, total):
        self.num = num
        self.total_num = total

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        self._num = num

    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        if total_num < 0:
            raise ValueError
        self._total_num = total_num

    def percentage(self):
        result = self.num / self.total_num * 100
        return result


m1 = MarksheetPercentage(599, 700)
print(m1.percentage())

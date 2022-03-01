
class Prime:
    def __init__(self, end=100):
        self.num = 2
        self.end = end

    def __iter__(self):
        return self

    def is_prime(self):
        i = 2
        while i <= self.num//2:
            if self.num % i == 0:
                return False
            i += 1
        return True

    def __next__(self):
        if self.num < self.end:
            if self.is_prime():
                num1 = self.num
                self.num += 1
                return num1
            else:
                self.num += 1
                return ''
        else:
            raise StopIteration


p1 = Prime()
it = iter(p1)
# print(p1.is_prime())
for i in p1:
    # if not i == None:
    #     print(i)
    print(i)

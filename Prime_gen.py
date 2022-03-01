
def is_prime(n):
    i = 2
    while i <= n//2:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_gen(end=100):
    num = 2
    while num < end:
        if is_prime(num):
            yield num
            num += 1
        else:
            num += 1


print(is_prime(17))
p1 = prime_gen()
for i in p1:
    print(i)

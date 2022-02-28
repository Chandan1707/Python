
def second(func):
    msg = 'hi'

    def inner():
        print('inside inner', msg)
        func()
        print('bye')
    return inner


@second
def first():
    print('hello')


first()

# last line added

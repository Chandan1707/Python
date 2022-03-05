class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return 'stack is empty'
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


s1 = Stack()
s1.push(20)
s1.push(34)
s1.push(344)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

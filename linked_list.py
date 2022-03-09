class Node:
    def __init__(self, val):
        self.info = val
        self.next = None

    def __repr__(self):
        return f"< Node : {self.info}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def __str__(self):
        current = self.head
        temp_list = []
        while current is not None:
            if current is self.head:
                temp_list.append(f'Head : {self.head.info}')
            elif current.next is None:
                temp_list.append(f'Tail : {current.info}')
            else:
                temp_list.append(f'{current.info}')
            current = current.next
        return f'{temp_list}'

    def add_node(self, val):
        new = Node(val)
        if self.head is None:
            self.head = new
            self.current = new
        else:
            self.current.next = new
            self.current = self.current.next

    def add_at_pos(self, val, pos):
        current = self.head
        new = Node(val)
        if pos == 1:
            new.next = self.head
            self.head = new

        while pos > 2:
            if current.next is None:
                raise IndexError("position out of range")
            current = current.next
            pos -= 1
        new.next = current.next
        current.next = new

    def delete_value(self, val):
        current = self.head
        prev = None
        while current is not None:
            if current.info is val:

                if current is self.head:
                    self.head = self.head.next
                    current = self.head
                    continue

                prev.next = current.next
            prev = current
            current = current.next

    def delete_at_pos(self, pos):
        current = self.head
        if pos == 1:
            self.head = self.head.next
        while pos > 2:
            pos -= 1
        current.next = current.next.next

    def search(self, val):
        current = self.head
        while current is not None:
            if current.info == val:
                return True
            current = current.next
        return False

    def find_max(self):
        current = self.head.next
        max_val = self.head.info
        while current is not None:
            if current.info > max_val:
                max_val = current.info
            current = current.next
        return max_val


l1 = LinkedList()
l1.add_node(10)
l1.add_node(20)
l1.add_node(30)
l1.add_node(40)
print(l1)
l1.add_at_pos(50, 5)
print(l1)
l1.delete_value(10)
print(l1)
l1.delete_at_pos(3)
print(l1)
print('Search 90:', l1.search(90))
print('Search 20:', l1.search(20))
print('Max value :', l1.find_max())

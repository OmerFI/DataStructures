class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({self.value})"


class CircularLinkedList:
    def __init__(self, value):
        self.length = 1
        self.tail = Node(value)

    def __len__(self):
        return self.length

    def __iter__(self):
        self._traversed = self.traverse()
        return self

    def __next__(self):
        return next(self._traversed).value

    @property
    def head(self):
        if self.length == 1:
            return self.tail
        return self.tail.next

    @head.deleter
    def head(self):
        if self.length == 1:
            raise Exception(
                "Could not delete because length of CircularLinkedList is equal to 1"
            )
        del self.tail.next

    def add_to_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.tail.next = node
        self.length += 1

    def add_to_end(self, value):
        head = self.head
        node = Node(value)
        node.next = head
        self.tail.next = node
        self.tail = node
        self.length += 1

    def remove_head(self):
        new_head = self.head.next
        del self.head
        self.tail.next = new_head
        self.length -= 1
        return new_head

    def remove_tail(self):
        current = self.head
        while True:
            if current.next is self.tail:
                break
            current = current.next
        current.next = self.head

        del self.tail
        self.tail = current
        self.length -= 1
        return current

    def remove_at(self, index):
        if index > self.length - 1:
            raise IndexError

        for idx, node in enumerate(self.traverse(length=index)):
            if idx == index - 1:
                break
        # now node's index is index - 1
        new_next = node.next.next
        deleted_next = node.next
        del node.next
        node.next = new_next
        self.length -= 1
        return deleted_next

    def traverse(self, **kwargs):
        length = kwargs.get("length", self.length)
        current = self.head
        for i in range(0, length):
            yield current
            current = current.next

    def print_all(self, **kwargs):
        for node in self.traverse():
            print(node.value, **kwargs)


print("=====")
c = CircularLinkedList(5)
c.add_to_end(2)
c.add_to_end(3)
c.add_to_beginning(4)
c.print_all()  # 4 5 2 3
print("=====")
c.remove_at(2)
c.print_all()  # 4 5 3
print("=====")
print(list(c))  # [4, 5, 3]

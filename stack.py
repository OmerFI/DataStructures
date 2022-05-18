class Stack(list):
    def __init__(self, *args, **kwargs) -> None:
        return super().__init__(*args, **kwargs)

    def is_empty(self) -> bool:
        return len(self) == 0

    def push(self, *args, **kwargs):
        return self.append(*args, **kwargs)


mylist = Stack([1, 2, 3])
mylist.push(7)
print(mylist)  # [1, 2, 3, 7]
mylist.push(4)
mylist.push(24)
mylist.pop()
print(mylist)  # [1, 2, 3, 7, 4]

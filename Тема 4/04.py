class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self._items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека."""
        if self.is_empty():
            raise IndexError("pop из пустого стека")
        return self._items.pop()

    def is_empty(self):
        """Возвращает True, если стек пуст."""
        return len(self._items) == 0

    def peek(self):
        """Возвращает элемент с вершины стека без удаления."""
        if self.is_empty():
            raise IndexError("peek из пустого стека")
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"

s = Stack()
print(s.is_empty())

s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.pop())
print(s.is_empty())
print(s.peek())
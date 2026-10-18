from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self._items.append(item)

    def dequeue(self):
        """Удаляет и возвращает первый элемент очереди."""
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        return self._items.popleft()

    def is_empty(self):
        """Возвращает True, если очередь пуста."""
        return len(self._items) == 0

    def peek(self):
        """Возвращает первый элемент без удаления."""
        if self.is_empty():
            raise IndexError("peek из пустой очереди")
        return self._items[0]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"

q = Queue()
print(q.is_empty())

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q.peek())
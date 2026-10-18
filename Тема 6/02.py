class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("peek из пустой очереди")
        return self._items[0]


def process_tasks(tasks):
    """
    tasks: список кортежей (название_задачи, время_выполнения_в_секундах)
    Выводит момент времени, когда каждая задача завершится.
    """
    q = Queue()
    for task in tasks:
        q.enqueue(task)

    current_time = 0.0
    print(f"{'Задача':<15} | {'Время':>8} | {'Завершение':>12}")
    print("-" * 42)

    while not q.is_empty():
        name, duration = q.dequeue()
        start_time = current_time
        current_time += duration
        print(f"{name:<15} | {duration:>8.2f} | {current_time:>10.2f} с")

    print("-" * 42)
    print(f"Общее время обработки всех задач: {current_time:.2f} с")

tasks = [
    ("Скачать файл", 2.5),
    ("Проверить почту", 1.0),
    ("Скомпилировать", 4.2),
    ("Отправить отчёт", 0.8),
    ("Резервная копия", 3.0),
]

process_tasks(tasks)
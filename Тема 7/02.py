class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1

        if self.count / self.size > 0.75:
            self.resize()

    def search(self, key):
        for k, v in self.table[self._hash(key)]:
            if k == key:
                return v
        return None

    def delete(self, key):
        bucket = self.table[self._hash(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def resize(self):
        """Увеличивает размер таблицы вдвое и перераспределяет элементы."""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for k, v in bucket:
                self.insert(k, v)

    def load_factor(self):
        return self.count / self.size

    def __repr__(self):
        items = [f"{k!r}: {v!r}" for bucket in self.table for k, v in bucket]
        return "{" + ", ".join(items) + "}"

ht = HashTable(size=5)
print(f"Начальный размер: {ht.size}, load_factor = {ht.load_factor():.2f}")

for i in range(1, 11):
    ht.insert(f"key{i}", i * 100)
    print(f"Добавлен key{i}: size = {ht.size}, count = {ht.count}, "
          f"load_factor = {ht.load_factor():.2f}")

print("\nИтоговая таблица:", ht)
print("Поиск key7:", ht.search("key7"))
print("Поиск key10:", ht.search("key10"))
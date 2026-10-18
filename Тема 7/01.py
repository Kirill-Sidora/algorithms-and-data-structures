class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        """Простая хеш-функция на основе встроенного hash()."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Вставляет пару (key, value) или обновляет значение."""
        index = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1

    def search(self, key):
        """Возвращает значение по ключу или None."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Удаляет пару по ключу. Возвращает True при успехе."""
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def __repr__(self):
        items = [f"{k!r}: {v!r}" for bucket in self.table for k, v in bucket]
        return "{" + ", ".join(items) + "}"

ht = HashTable(size=5)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)

print(ht.search("banana"))
print(ht.search("grape"))

ht.delete("banana")
print(ht.search("banana"))
print(ht)
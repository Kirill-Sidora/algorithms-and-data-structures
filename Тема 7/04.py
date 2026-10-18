def simple_hash(s):
    return sum(ord(ch) for ch in s)

class HashDictionary:
    """Словарь {строка: хеш-значение} на основе цепочек."""

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _index(self, key):
        return simple_hash(key) % self.size

    def add(self, key):
        """Добавляет строку; значением становится её хеш-значение."""
        value = simple_hash(key)
        index = self._index(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        """Возвращает хеш-значение по ключу или None, если ключа нет."""
        index = self._index(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def __repr__(self):
        items = [f"{k!r}: {v}" for bucket in self.table for k, v in bucket]
        return "{" + ", ".join(items) + "}"

d = HashDictionary()

words = ["apple", "banana", "cherry", "date", "fig"]
for w in words:
    d.add(w)

print("Словарь:", d)

for w in ["apple", "cherry", "grape"]:
    result = d.get(w)
    if result is None:
        print(f"'{w}' — не найден")
    else:
        print(f"'{w}' → {result}")

print("\nПроверка коллизий:")
print(f"hash('abc') = {simple_hash('abc')}, "
      f"hash('cba') = {simple_hash('cba')}")
d.add("abc")
d.add("cba")
print(d.get("abc"), d.get("cba"))
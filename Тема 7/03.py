def simple_hash(s):
    """Возвращает сумму ASCII-кодов всех символов строки."""
    return sum(ord(ch) for ch in s)

print(simple_hash("hello"))
print(simple_hash("abc"))
print(simple_hash(""))
print(simple_hash("abc"))
print(simple_hash("cba"))
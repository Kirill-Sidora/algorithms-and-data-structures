# 01
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 02
# O(n). Чем больше элементов в массиве, тем сложнее

# 03
import random
import time

def test_search(arr, target):
    start = time.perf_counter()
    idx = linear_search(arr, target)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Ищем {target}: индекс = {idx}, время = {elapsed_ms:.4f} мс")

numbers = [random.randint(1, 200) for _ in range(100)]

print("Список:", numbers)
test_search(numbers, 5)
test_search(numbers, 13)
test_search(numbers, 42)
test_search(numbers, 52)
test_search(numbers, 67)

# 04
sizes = [10, 100, 1000, 10000, 100000]

for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    linear_search(arr, -1)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Размер: {n}, время: {elapsed_ms:.4f} мс")
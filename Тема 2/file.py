# 01
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 02
# O(log n). На каждом шаге количество элементов сокращается вдвое

# 03
import random
import time

def test_search(arr, target):
    start = time.perf_counter()
    idx = binary_search(arr, target)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Ищем {target}: индекс = {idx}, время = {elapsed_ms:.4f} мс")

numbers = sorted(random.randint(1, 200) for _ in range(100))

print("Список:", numbers)
test_search(numbers, 5)
test_search(numbers, 13)
test_search(numbers, 42)
test_search(numbers, 52)
test_search(numbers, 67)

# 04
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sizes = [10, 100, 1000, 10000, 100000]

print("Линейный поиск:")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    linear_search(arr, -1)
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")

print("Бинарный поиск:")
for n in sizes:
    arr = sorted(random.randint(1, n * 10) for _ in range(n))
    start = time.perf_counter()
    binary_search(arr, -1)
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")
# 01
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 02
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 03
import random
import time
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sizes = [10, 100, 500, 1000, 2000]

print("Сортировка пузырьком:")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    bubble_sort(arr.copy())
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")

print("Сортировка выбором:")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    selection_sort(arr.copy())
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")

print("Сортировка вставками:")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    insertion_sort(arr.copy())
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")
import random
import time

def quicksort(arr):
    """Быстрая сортировка (рекурсивная, через подсписки)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)

def insertion_sort(arr):
    """Сортировка вставками (in-place)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sizes = [10, 100, 500, 1000, 2000]

print("Быстрая сортировка (QuickSort):")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    quicksort(arr.copy())
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")

print("\nСортировка вставками:")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    insertion_sort(arr.copy())
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")
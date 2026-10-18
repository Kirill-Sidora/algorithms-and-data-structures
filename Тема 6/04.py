import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sizes = [10, 100, 500, 1000, 2000]

print("Сортировка слиянием (MergeSort):")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    merge_sort(arr.copy())
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")

print("\nСортировка пузырьком:")
for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    start = time.perf_counter()
    bubble_sort(arr.copy())
    end = time.perf_counter()
    print(f"Размер: {n}, время: {(end - start) * 1000:.4f} мс")
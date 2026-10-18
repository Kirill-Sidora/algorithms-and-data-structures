def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(less) + equal + quicksort(greater)

data = [10, 7, 8, 9, 1, 5, 3, 6, 2, 4]
print("До:", data)
sorted_data = quicksort(data)
print("После:", sorted_data)
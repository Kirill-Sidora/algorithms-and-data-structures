def binary_search(arr, target, low = 0, high = None):

    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(sorted_list, 7))
print(binary_search(sorted_list, 1))
print(binary_search(sorted_list, 15))
print(binary_search(sorted_list, 4))
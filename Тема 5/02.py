def find_max(lst):

    if len(lst) == 1:
        return lst[0]

    mid = len(lst) // 2
    left_max = find_max(lst[:mid])
    right_max = find_max(lst[mid:])

    return left_max if left_max > right_max else right_max

print(find_max([3, 7, 2, 9, 1, 5]))
print(find_max([50]))
print(find_max([-5, -2, -10, -1]))
def findMaxMin(arr, i, j):
    # small problem
    # single element presmt in an array
    if i == j:
        max_val = arr[i]
        min_val = arr[i]
    # Two element is present in an array
    elif i == j - 1:
        if arr[i] < arr[j]:
            min_val = arr[i]
            max_val = arr[j]
        else:
            max_val = arr[i]
            min_val = arr[j]

    # big problem
    else:
        mid = i + (j - i) // 2
        max_l, min_l = findMaxMin(arr, i, mid)
        max_r, min_r = findMaxMin(arr, mid + 1, j)

        if max_l < max_r:
            max_val = max_r
        else:
            max_val = max_l

        if min_l < min_r:
            min_val = min_l
        else:
            min_val = min_r

    return max_val, min_val


# driver code
arr = [10, 24, 23, 84, 91, 90, 3, 2, 45]
i = 0
j = len(arr) - 1
max_val, min_val = findMaxMin(arr, i, j)
print(f'Maximum element is :- {max_val} and minimum value is :- {min_val}')
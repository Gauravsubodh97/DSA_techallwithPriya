def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# driver code
arr = [45, 34, 20, 164, 101, 78]
result = bubbleSort(arr)
print('After appling the bubble sort on the array: ', result)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# driver code
arr = [20, 13, 7, 9, 99, 55, 76]
result = bubbleSort(arr)
print(result)
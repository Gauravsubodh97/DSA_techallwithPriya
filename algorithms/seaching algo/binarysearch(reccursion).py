def binarySearch(arr, i, j, k):
    if j >= i:
        mid = i + (j - i) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return binarySearch(arr, i, mid - 1, k)
        elif arr[mid] < k:
            return binarySearch(arr, mid + 1, j, k)
    else:
        return -1


# driver code
arr = [3, 4, 5, 6, 7, 8, 9, 11, 14, 16, 18, 19, 191, 201, 401, 444]
key = 8
result = binarySearch(arr, 0, len(arr) - 1, key)
print(result)

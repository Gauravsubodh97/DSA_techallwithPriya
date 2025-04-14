def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # Left and right halves
        leftsubtree = arr[:mid]
        rightsubtree = arr[mid:]

        # Recursively sort both halves
        mergeSort(leftsubtree)
        mergeSort(rightsubtree)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(leftsubtree) and j < len(rightsubtree):
            if leftsubtree[i] < rightsubtree[j]:
                arr[k] = leftsubtree[i]
                i += 1
            else:
                arr[k] = rightsubtree[j]
                j += 1
            k += 1

        # Copy any remaining elements of leftsubtree
        while i < len(leftsubtree):
            arr[k] = leftsubtree[i]
            i += 1
            k += 1

        # Copy any remaining elements of rightsubtree
        while j < len(rightsubtree):
            arr[k] = rightsubtree[j]
            j += 1
            k += 1


# Driver code
arr = [80, 42, 45, 73, 12, 34, 56]
mergeSort(arr)
print(arr)
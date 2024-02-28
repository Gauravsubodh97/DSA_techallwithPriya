def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i],arr[min_idx] = arr[min_idx] , arr[i]
    return arr

#driver code
arr =[ 12,9,6,77,45,23,2,78,89,34,45]
result =selectionSort(arr)
print(result)

def selectionSorting(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

sol = selectionSorting(arr)
print('my solution is :',sol)

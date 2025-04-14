def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx =i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
         #swap
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

#driver code
arr =[50,60,44,12,4,16,19,99,34]
result= selectionSort(arr)
print('Sorted array after applying selection sorting algorithm: ', result)
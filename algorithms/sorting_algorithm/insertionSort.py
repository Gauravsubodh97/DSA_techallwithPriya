def insertionSort(arr):

    for i in range(len(arr)):

        key = arr[i]
        j = i -1
        while j >=0 and key < arr[j]:



    return arr





#driver code
arr =[4,8,1,4,5,3]
result = insertionSort(arr)
print(result)
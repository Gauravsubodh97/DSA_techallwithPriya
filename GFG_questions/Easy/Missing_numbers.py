
def missingNum(arr):
    arr.sort()
    n = len(arr)-1
    for i in range(0, n):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i]+1


#driver code
arr  = [11,12,13,15,16]
result = missingNum(arr)
print(result)
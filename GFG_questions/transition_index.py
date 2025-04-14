def tansition_index(arr):
    n =len(arr)
    for i in range(1,n):
        if arr[i] + arr[i+1] == 1:
            return i+1
    return -1



#driver code
arr =[0,0,0,0,0,0]
result = tansition_index(arr)
print(result)
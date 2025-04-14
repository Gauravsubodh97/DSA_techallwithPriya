def binarysea(arr,i,j,x):
    if j >=i:
        mid = i + (j - i) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysea(arr,i,mid-1,x)
        elif arr[mid] < x:
            return binarysea(arr,mid+1,j,x)
    else:
        return -1

arr =[20,30,40,50,60,80,90,101,201]
key = 40
result = binarysea(arr,0,len(arr)-1,key)
print(result)

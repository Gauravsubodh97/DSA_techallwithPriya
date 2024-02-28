

def binarysearch(arr,i,j,k):

    while j>=i:
        mid = i+(j-i)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            j = mid -1
        elif arr[mid] < k:
            i = mid +1
    return -1

#driver code
arr =[5,6,7,8,9,10,44,55,66,77,88,101,201,300]
key = 6
result =binarysearch(arr,0,len(arr)-1,key)
print(result)
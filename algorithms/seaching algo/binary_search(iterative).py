def binarsearch(arr,i,j,key):

    while j >=i :
        mid = i+(j-i) //2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            j =mid -1
        elif arr[mid] < key:
            i =mid+1

    else:
        return -1

#driver code
arr =[10,20,30,40,50,60,70,80,90,100,101,201,301]
key =50
result =binarsearch(arr,0,len(arr)-1,key)
print(result)




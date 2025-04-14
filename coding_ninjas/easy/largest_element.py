
def largeEle(arr):
    lrg =0
    n =len(arr)
    for i in range(n):
        if arr[i] > lrg:
            lrg =arr[i]
    return lrg

#driver code
arr =[2,3,4,5,6]
result = largeEle(arr)
print(result)
def missingNum(arr):
    n =len(arr)
    exp_sum = n*(n+1)//2
    sums = sum(arr)

    return exp_sum -sums

# driver code
arr=[1,2,3,5]
result = missingNum(arr)
print(result)
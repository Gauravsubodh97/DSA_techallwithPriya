def removeDuplicate(nums):
    i=0
    while i < len(nums):
        if nums.count(nums[i]) > 2:
            nums.pop(i)
        else:
            i+=1
    return nums
nums = nums = [0,0,1,1,1,1,2,3,3]
result =  removeDuplicate(nums)
print(result)
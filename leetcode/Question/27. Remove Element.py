def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if val != nums[j]:
            nums[i] = nums[j]
            i += 1
    return i
nums = [0,1,2,2,3,0,4,2]

val = 2
result= removeElement(nums, val)
print(result)
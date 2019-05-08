def trap(nums):
    movepeak = 0
    triprain = 0
    maxindex = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[maxindex]:
            maxindex = i
    
    for j in range(maxindex):
        if movepeak < nums[j]:
            movepeak = nums[j]
        else:
            triprain += movepeak - nums[j]
    
    movepeak = 0

    for k in range(len(nums)-1, maxindex, -1):
        if movepeak < nums[k]:
            movepeak = nums[k]
        else:
            triprain += movepeak - nums[k]
    
    return triprain


nums =  [0,1,0,2,1,0,1,3,2,1,2,1]
res = trap(nums)
print(res)
def quick_sort(nums, left, right):
    if left>=right:
        return
    pivot = part(nums, left, right)
    quick_sort(nums, left, pivot-1)
    quick_sort(nums, pivot+1, right)

def part(nums, left, right):
    key = nums[right]
    i = left
    for j in range(left, right):
        if nums[j]<=key:
            nums[i], nums[j]=nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i
















nums = [9,69,2,42,6,5,6,1,47,]
quick_sort(nums, 0, len(nums)-1)
print(nums)
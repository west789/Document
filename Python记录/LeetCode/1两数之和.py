

def twoSum(nums, target):
    '''
    :type nums: List[int]
    :type target: int
    '''
    # 暴力法(穷举法)
    # count = len(nums)
    # for i in range(count):
    #     for j in range(i+1, count):
    #         if nums[i] + nums[j] == target :
    #             print('输出值', i, j)


    # 一次遍历
    count = len(nums)
    itemDict = {nums[i]: i for i in range(count)}
    for i in range(count):
        cha = target - nums[i]
        if cha in itemDict.keys() and itemDict[cha] != i:
            print(i, itemDict[cha])
            break
if __name__ == '__main__':
    nums = [5,6,8,9,1,2]
    target = 17
    twoSum(nums, target)
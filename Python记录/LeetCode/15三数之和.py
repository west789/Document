

def doMain(nums):
    # res = []
    # for i in range(len(nums)-2):
    #     for j in range(i+1, len(nums)-1):
    #         for k in range(j+1, len(nums)):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 sortList = [nums[i],  nums[j], nums[k]]
    #                 print(sortList)
    #                 sortList.sort()
    #                 res.append(sortList)
    # resNew = [list(i) for i in set(tuple(_) for _ in res)]
    # resNew.sort(key=res.index)
    # print (resNew)
    # return resNew

    if len(nums) <= 2:
            return []
        
        # 存储结果列表
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                if nums[j] + nums[k] + nums[i] == 0:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j+1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                else:
                    k -= 1
        return res_list

if __name__ == '__main__':
    nums = [0,0,0,0,0]
    doMain(nums)
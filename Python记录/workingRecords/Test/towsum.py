def two_sum(nums, sum_num):
    dict_num = {}
    res = []
    for i, item in enumerate(nums):
        if item in dict_num:
            res.append((dict_num[item], i))
        else:
            dict_num[sum_num-item] = i
    return res
if __name__ == "__main__":
    sum_num = 10
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(two_sum(nums, sum_num))
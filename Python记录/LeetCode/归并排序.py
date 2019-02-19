def MergeTwo(left, right):
    resSort = []
    lindex, rindex = 0, 0
    while True:
        if left[lindex]>right[rindex]:
            resSort.append(right[rindex])
            rindex += 1
        else:
            resSort.append(left[lindex])
            lindex += 1
        if lindex==len(left) or rindex==len(right):
            break
    resSort.extend(left[lindex:])
    resSort.extend(right[rindex:])
    return resSort
def MergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right  = MergeSort(arr[mid:])
    return MergeTwo(left, right)

arr = [5, 6, 12, 9, 6, 99, 50]
res = MergeSort(arr)
print(res)
def mergesort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


seq = [5, 3, 0, 6, 1, 4]
print('排序前：', seq)
result = mergesort(seq)
print('排序后：', result)


# if __name__ == "__main__":
#     unSortedList = [5, 9, 56, 1, 2, 65]
#     mergesort(unSortedList) fdsgdf

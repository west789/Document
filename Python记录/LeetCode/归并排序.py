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
# 冒泡排序
# def bubbleSort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# arr = [1, 2, 9, 5, 6, 3]
# bubbleSort(arr)

#插入排序
# def insertSort(arr):
#     n = len(arr)
#     if n <=1:
#         return arr
#     for i in range(1, n):
#         for j in range(i, 0, -1):
#             if arr[j-1]>arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#             else:
#                 break
#     print (arr)

# arr = [1,4,2,3,76,66,99]
# insertSort(arr)

#选择排序
def chooseSort(arr):
    n = len(arr)
    for i in range(0, n):
        min_num = i
        for j in range(i+1, n):
            if arr[min_num]>arr[j]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]
    print(arr)


arr = [5, 3, 9, 56, 22, 23, 10]
chooseSort(arr)
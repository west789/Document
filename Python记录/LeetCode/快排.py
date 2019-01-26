# def QuickSort(arr):
#     if len(arr)==1:
#         return arr
#     mid = len(arr) // 2
#     left, right = 0, len(arr)
#     if left == right:
#         QuickSort(arr[:mid])
#         QuickSort(arr[mid:])
#     while left<=right:
#         if arr[left]<=mid:
#             left += 1
#         else:
#             break
#     while 
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)

arr = [6, 9, 88, 50, 6, 12, 16]
quick_sort(arr, 0, len(arr)-1) 
print (arr)
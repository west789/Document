<<<<<<< HEAD
def quick_sort(arr, low, high):
    if low<high:
        q = partition(arr, low, high)
        quick_sort(arr, low, q-1)
        quick_sort(arr, q+1, high)

def partition(arr, low, high):
    x = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j]<=x:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


arr = [6, 3, 5, 4, 2, 3]
print (arr)
quick_sort(arr, 0, len(arr)-1)
=======
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
>>>>>>> e432abd78df0849c0870560b1a1f9d838f3850b0
print (arr)
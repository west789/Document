# def quick_sort(array, l, r):
#     if l < r:
#         q = partition(array, l, r)
#         quick_sort(array, l, q - 1)
#         quick_sort(array, q + 1, r)
 
# def partition(array, l, r):
#     x = array[r]
#     i = l - 1
#     for j in range(l, r):
#         if array[j] <= x:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[r] = array[r], array[i+1]
#     return i + 1

def quick_sort(arr, l, r):
    if l<r:
        q = partition(arr, l, r)
        quick_sort(arr, l, q-1)
        quick_sort(arr, q+1, r)

def partition(arr, l, r):
    x = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j]<=x:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

arr = [3,2,5,14,12]
quick_sort(arr, 0, len(arr)-1)
print(arr)
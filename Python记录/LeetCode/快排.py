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
print (arr)
#循环实现
def bSerarch(arr, n, value):
    high = n-1
    low = 0
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==value:
            return mid
        if arr[mid]<value:
            low = mid+1
        else:
            high = mid-1
    return -1

#递归实现
def bSerarch1(arr, n, value):
    return bSerarchInter(arr, 0, n-1, value)

def bSerarchInter(arr, low, high, value):
    mid = (low+high)//2
    if low>high:
        return -1
    if arr[mid] == value:
        return mid
    if arr[mid]<value:
        return bSerarchInter(arr, mid+1, high, value)
    else:
        return bSerarchInter( arr, low, mid-1, value)

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
pivot = bSerarch(arr, len(arr), 9)
print ("循环实现", pivot)
pivot1 = bSerarch1(arr, len(arr), 9)
print ("递归实现", pivot1)
def search(arr, ele):
    length = len(arr)
    left = 0
    right = length - 1
    counter = 0
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == ele: return mid, counter
        elif arr[mid] < ele: left = mid+1
        else: right = mid-1
        counter += 1
    else: return -1

'''def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(sort([1,2,5,5,7,785,7,65,548,6,6,8,684,6,468]))'''


def sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j>= 0:
            if key > lst[j]:
                lst[j+1] = lst[j]
                lst[j] = key
                j -= 1
            else:
                break
            
    return lst

print(sort([1,2,5,5,7,785,7,65,548,6,6,8,684,6,468]))
print(sort([7,1,3,5,9,3]))



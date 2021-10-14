'''def sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(sort([1,5,6,8,9,4,3,7,-1,4,6,9,2,8,6]))'''


def sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]>lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    yield lst
print([x for x in sort([1,54,54,8,76,5,4,16,6,4648,4,8,6])])
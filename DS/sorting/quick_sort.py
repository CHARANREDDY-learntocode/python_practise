'''def sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot =arr.pop()
        items_greater = []
        items_lesser = []
        for item in arr:
            if pivot > item: items_lesser.append(item)
            else: items_greater.append(item)

        return sort(items_lesser) + [pivot] + sort(items_greater)

print(sort([10,2,5,4,468,4,368,6,68,4,45]))'''

def sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        items_lesser= []
        items_greater = []
        for item in arr:
            if item > pivot: items_greater.append(item)
            else: items_lesser.append(item)
        return sort(items_lesser) + [pivot] + sort(items_greater)

print(sort([10,2,5,4,468,4,368,6,68,4,45]))
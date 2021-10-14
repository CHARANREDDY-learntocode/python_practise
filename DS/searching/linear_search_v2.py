'''def search(lst, ele):
    left = 0
    right = len(lst)-1
    position = -1
    length =len(lst)

    for left in range(0, right):
        if lst[left] ==ele:
            position = left
            print(f'{ele} found at position {position} in attempt {left + 1}')
            break
        if lst[right] == ele:
            position = right
            print(f'{ele} found at position {position} in attempt {left + 1}')
            break

        right -= 1

    if position == -1: print('{} not found'.format(position))

arr = [x for x in range(10)]
search(arr, 9)'''

def search(lst, ele):
    left = 0
    right = len(arr)-1
    position = -1

    for left in range(0, right):
        if lst[left] == ele:
            position = left
            break
        if lst[right] == ele:
            position=right
            break
        right -= 1

    return position

arr = [1,986,686,68,67,94,86,64,7,9,6,7,4,76,9]
print(search(arr, 9))


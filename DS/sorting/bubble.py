def sort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(sort([1,2,3,5,5,8,7,85,5,4,454,6,468,6,6,4,86,6,468,64,6]))

print(sort([1,156,68,45,468,6,68,6,48,68,8468,984]))

def binarySearch(arr,beg,end,item):  
    if end >= beg:  
        mid = int((beg+end)/2)  
        if arr[mid] == item :  
            return mid+1  
        elif arr[mid] < item :   
            return binarySearch(arr,mid+1,end,item)  
        else:   
            return binarySearch(arr,beg,mid-1,item)  
    return -1  
      
  
arr=[x for x in range(100, 0,-1)];  
item = int(input("Enter the item which you want to search ?"))  
location = -1;   
location = binarySearch(arr,0,9,item);  
if location != -1:   
    print("Item found at location %d" %(location))  
else:   
    print("Item not found")
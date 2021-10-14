def sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        L = lst[:mid]
        R = lst[mid:]
        sort(L)
        sort(R)

        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[i]:
                lst[k] = L[i]
                i+=1
            else:
                lst[k] = R[i]
                j += 1
            k += 1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j+=1
            k+=1

arr = [1,2,5,8,1000,4,5,4,8,8,9,9,10,6,8]
sort(arr)
print(arr)
dim = int(input('Dimensions: '))
lst = [[(1+i*dim + j) for j in range(5)]for i in range(5)]
col = 2
res = [lst[row][2] for row in range(len(lst))]
print(res)  

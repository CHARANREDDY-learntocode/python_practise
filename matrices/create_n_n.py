from itertools import count

dim = int(input('Enter the Dimension value: '))

rez = [[((1+dim*i + j)) for j in range(dim)] for i in range(dim)]
print(rez)
#using count

temp = count(1)
rez = [[next(temp) for j in range(dim)] for i in range(dim)]
print(rez)
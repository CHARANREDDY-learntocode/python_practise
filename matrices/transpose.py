
import numpy as np
x = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]

trans_of_x = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

print("original list:", x)
print("Tranpose of list:", trans_of_x)

#using zip
print(list(zip(*x)))

#using numpy
print(np.transpose(x))
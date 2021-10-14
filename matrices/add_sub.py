x = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
y = [[3,4,5,6], [1,2,3,4], [2,3,4,5]]

result = []

#add two matrices
for i in range(len(x)):
    temp_list = []
    for j in range(len(x[0])):
        temp_list.append(x[i][j] + y[i][j])
    result.append(temp_list)
print('addition: ', result)

result = []
#substract two matrices
for i in range(len(x)):
    temp_list = []
    for j in range(len(x[0])):
        temp_list.append(x[i][j] - y[i][j])
    result.append(temp_list)

print('substraction: ', result)
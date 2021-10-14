x = [[1,2,3,4],
[5,6,7,8],
[1,2,3,4]]

y = [[1,2,3,4],
[5,6,7,8],
[1,2,3,4]]

result = [[0,0,0, 0],
		[0,0,0, 0],
		[0,0,0, 0]]

# iterate through rows
for i in range(len(x)):
# iterate through columns
	for j in range(len(x[0])):
		result[i][j] = x[i][j] + y[i][j]

for r in result:
	print(r)

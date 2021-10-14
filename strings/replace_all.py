test_str = 'geeksforgeeks'
temp = str.maketrans("geek", "abcd")
test_str = test_str.translate(temp)

print(test_str)
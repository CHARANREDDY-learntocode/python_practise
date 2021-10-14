def add_three(x):
    if x % 2 == 0:
        return True        
    else:
        return False
li = [1,2,3,4,5,6,7,8]
print(print filter(add_three, li))
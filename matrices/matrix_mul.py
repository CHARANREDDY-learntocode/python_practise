from itertools import chain

def product(lst):
    result = 1
    for sub_list in lst:
        for ele in sub_list:
            result *= ele
    return result

lst = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

print(product(lst))

#using chain method from itertools
result = 1
for val in chain(*lst):
    result *= val

print('using itertools method', result) 
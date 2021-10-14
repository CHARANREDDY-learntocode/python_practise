def primes(start, end):
    for i in range(start, end):
        if i>1:
            for j in range(2, i//2+1):
                if i%j == 0:
                    break
            else:
                print(i)

primes(1,30)

def fibinacci(range):
    prev = 0
    current = 1
    print(prev, current, end=' ')
    val = 0
    while True:
        val = prev + current
        if val > range: break
        print(val, end=' ')
        prev = current
        current = val

#fibinacci(100)

def Cloning(li1):
    li_copy =[]
    li_copy = li1.copy()
    return li_copy
  
# Driver Code
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# li1.append(10)
# print("Original List:", li1)
# print("After Cloning:", li2)

#Cumulative sum of a list
def cumulative_list(lst):
    cum_list = []
    cum_sum = 0
    for num in lst:
        cum_list.append(num + cum_sum)
        cum_sum += num
    return cum_list

#print(cumulative_list([10, 20, 30, 40, 50]))

#Break a list into chunks of size N in Python
def create_chunks(l, size):
    for i in range(0, len(l), size):
        yield l[i:i+size]

#gen = create_chunks(list(range(20)), 4)
#print(list(gen))

#map function
def square(num):
    return num*2

print([num for num in map(square, [1,2,3,5,4,5,58,7,54468,65,8,5,65])])

#filter function
def even_or_odd(num):
    return True if not num%2 else False

print([num for num in filter(even_or_odd, [x for x in range(10)])])

#reduce function
from functools import reduce
def sum(x, y):
    return x+y

print(reduce(sum, [x for x in range(10)]))


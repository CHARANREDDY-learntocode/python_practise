def logger(func):
    def main(*args, **kwargs):
        print('logged information')
        func(*args, **kwargs)

    return main

@logger
def calc_sum(lst):
   print(type({i:i**2 for i in range(100)}))

lst = [2,3,4,5,6]

calc_sum(lst)
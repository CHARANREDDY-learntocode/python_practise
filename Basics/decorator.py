def log(func):
    def log_func_called(*args, **kwargs):
            print('hello')
            func(*args, **kwargs)
    return log_func_called

@log
def print_args(*args, **kwargs):
    print(args, kwargs)

print_args(1,2,3,4,5,key1=0,key2=20)
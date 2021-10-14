def custom_range(start=0, stop=0, step=1):
    for i in range(start, stop, step):
        yield i

iter = custom_range(1,200,1)

for i in range(20):
    print(next(iter))

    


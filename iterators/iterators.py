class MyIter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self): return self
    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return current
        else: raise StopIteration




iter1 = MyIter(10, 20)
for i in iter1:
    print(i)
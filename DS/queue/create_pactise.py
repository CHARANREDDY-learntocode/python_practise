class Queue:
    def __init__(self, length):
        self.rear = 0
        self.front = self.size = 0
        self.Q = [None]*length
        self.length = length

    def is_full(self):
        return True if self.length == self.size else False

    def is_empty(self):
        return True if self.size == 0 else False

    def en_queue(self, item):
        if not self.is_full:
            self.rear = (self.rear+1)%self.size
            self.Q[self.rear] = item
            size += 1
            return self.Q
        else:
            raise IndexError("The Queue is full")
    def de_queue(self):
        if not self.is_empty():
            item = self.Q[self.front]
            self.front += 

            
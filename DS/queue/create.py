class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity
        self.capacity = capacity

    def is_full(self):
        if self.size == self.capacity: return True

    def is_empty(self):
        if self.size == 0: return True

    def en_queue(self, item):
        if self.is_full(): return True
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1
        return self.Q

    def de_queue(self):
        if self.is_empty(): return None
        item = self.Q[self.front]
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1
        return item

    def queue_front(self):
        if self.is_empty(): return None
        return self.Q[self.front]

    def queue_rear(self):
        if self.is_empty(): return None
        return self.Q[self.rear]


if __name__ == '__main__':
 
    queue = Queue(5)
    print(queue.en_queue(10))
    print(queue.en_queue(20))
    print(queue.en_queue(30))
    print(queue.en_queue(40))
    print(queue.en_queue(60))
    print(queue.de_queue())
    print(queue.queue_front())
    print(queue.queue_rear())
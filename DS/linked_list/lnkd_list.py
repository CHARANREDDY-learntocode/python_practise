class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        if not self.head: return 0
        temp = self.head
        counter = 0
        while(temp!=None):
            counter += 1
            temp = temp.next
        return counter

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return

        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node

    def insert(self, data, position):
        length = len(self)
        if position > length:
            raise IndexError('position should be in range of length of linked list')
        node = Node(data)
        temp = self.head
        current = 1
        while (current < position):
            prev = temp
            temp = temp.next
            current += 1
        
        node.next = prev.next
        prev.next = node
        return self

    def pop(self, position=None):
        if not position:
            temp = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            prev.next = None
            return temp.data
        else:
            if position <= len(self):
                temp = self.head
                if temp:
                    counter = 1
                    while counter < position:
                        prev = temp
                        temp = temp.next
                        counter += 1
                    prev.next = temp.next
                    return temp.data

    def list_data(self):
        if not self.head:
            return []
        else:
            lst = []
            temp = self.head
            while temp:
                lst.append(temp.data)
                temp = temp.next
            return lst
        
lnkd_lst = LinkedList()


lnkd_lst.append(1)
lnkd_lst.append(2)
lnkd_lst.append(3)
lnkd_lst.append(10)
lnkd_lst.append(11)
lnkd_lst.append(12)
print(lnkd_lst.list_data())
lnkd_lst.insert(4, 2)
print(lnkd_lst.list_data())
lnkd_lst.pop()
print(lnkd_lst.list_data())
lnkd_lst.pop(3)
print(lnkd_lst.list_data())
lnkd_lst.append(6)
print(lnkd_lst.list_data())






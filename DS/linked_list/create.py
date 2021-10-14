class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def node_data(self):
        temp = self.head
        counter = 1
        while temp != None:
            print(f'Node{counter}: ', temp.data)
            temp = temp.next
            counter += 1

    def push(self, data):
        head_node = Node(data)
        head_node.next = self.head 
        self.head = head_node

    def insert(self, prev_node, data):
        if not isinstance(prev_node, Node):
            raise TypeError(f"Expected prev_node type is {(Node.__name__).lower()}' got '{(type(prev_node).__name__).lower()}'")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        return new_node

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node


lnkd_lst = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

lnkd_lst.head = node1
node1.next = node2
node2.next = node3

#print the nodes data
print('Before operations:')
lnkd_lst.node_data()
#add the node at the start of list
lnkd_lst.push(5)
#add the node after the given node
lnkd_lst.insert(node2, 40)
#add the node at the end of list
lnkd_lst.append(50)
print('')
print('After Operations:')
#print the nodes data
lnkd_lst.node_data()
class Node:
    data:int
    next:"Node"
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class DataStructure: 
    def __init__(self, head = None):
        self.head = head

    def insert_front(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def interchange(self, major_node, minor_node):
        current_node = self.head 
        next_node = current_node.next    
        if next_node is not None:
            next_node2 = next_node.next
        if current_node.data == major_node.data and next_node.data == minor_node.data:
            self.head.next = next_node.next
            last_head = self.head
            next_node.next = last_head
            self.head = next_node

            return
        while (next_node2 is not None):
            if next_node.data == major_node.data and next_node2.data == minor_node.data:
                next_node.next = next_node2.next
                next_node2.next = next_node
                current_node.next = next_node2

                break
            else:
                current_node = next_node
                next_node = current_node.next
                next_node2 = next_node.next

    @property
    def size(self):
        current_node = self.head
        size = 0
        while(current_node is not None):
            current_node = current_node.next
            size += 1
        return size

    def print_all(self):
        print("Printing structure:")
        current_node = self.head
        while(current_node is not None):
            print(current_node.data, end = " ")
            current_node = current_node.next

d_structure = DataStructure()
d_structure.insert_front(27)
d_structure.insert_front(10)
d_structure.insert_front(500)
d_structure.insert_front(20)
d_structure.insert_front(14)

d_structure.print_all()

def bubble_sort (data_str):
    for outer_index in range(data_str.size):
        current_node = data_str.head
        next_node = current_node.next
        for i in range(data_str.size-1-outer_index):
            if current_node.data>next_node.data:
                data_str.interchange(current_node, next_node)
                next_node = current_node.next
            else:
                current_node = next_node
                next_node = current_node.next
            data_str.print_all()

            
bubble_sort(d_structure)
d_structure.print_all()

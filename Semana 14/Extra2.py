class Node:
    data:int
    next:"Node"
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList: 
    def __init__(self, head = None):
        self.head = head

    def insert_front(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_back(self, data):
        node = Node(data)
        next_node = self.head         
        while (next_node is not None):
            current_node = next_node
            next_node = current_node.next
        current_node.next = node

    def delete(self, data):
        current_node = self.head 
        next_node = current_node.next     
        if current_node.data == data:
            self.head = next_node
            return
        while (next_node is not None):
            if next_node.data == data:
                current_node.next = next_node.next
                break
            else:
                current_node = next_node
                next_node = current_node.next
        
    
    def print_all(self):
        print("Printing structure:")
        current_node = self.head
        while(current_node is not None):
            print(current_node.data, end = " ")
            current_node = current_node.next

l_list = LinkedList()
print("\nInserting element to the front")
l_list.insert_front(10)
l_list.print_all()
print("\nInserting element to the front")
l_list.insert_front(20)
l_list.print_all()
print("\nInserting element to the back")
l_list.insert_back(30)
l_list.print_all()
print("\nDeleting element")
l_list.delete(10)
l_list.print_all()

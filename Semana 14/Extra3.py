class Node:
    data:int
    next:"Node"
    previous: "Node"
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next
        
class LinkedList: 
    head: Node
    def __init__(self, head = None):
        self.head = head

class Double_Queue(LinkedList):
    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            next_node = current_node.next    
            while (next_node is not None):
                current_node = next_node
                next_node = current_node.next
            current_node.next = node
            node.previous = current_node

    def delete(self, data):
        current_node = self.head 
        next_node = current_node.next     
        if current_node.data == data:
            self.head = next_node
            self.head.previous = None
            return
        while (next_node is not None):
            if next_node.data == data:
                current_node.next = next_node.next
                if current_node.next is not None:
                    current_node.next.previous = current_node
                break
            else:
                current_node = next_node
                next_node = current_node.next
        
    def print_forward(self):
        print("Printing forward:")
        current_node = self.head
        while(current_node is not None):
            print(current_node.data, end = " ")
            current_node = current_node.next

    def print_backward(self):
        print("\nPrinting backward:")
        current_node = self.head
        while(current_node is not None):
            previous_node = current_node
            current_node = current_node.next
        while(previous_node is not None):
            print(previous_node.data, end = " ")
            previous_node = previous_node.previous

d_queue = Double_Queue()
print("\nInserting element to the end")
d_queue.append("A")
d_queue.print_forward()
d_queue.print_backward()
print("\nInserting element to the end")
d_queue.append("B")
d_queue.print_forward()
d_queue.print_backward()
print("\nInserting element to the end")
d_queue.append("C")
d_queue.print_forward()
d_queue.print_backward()
print("\nInserting element to the beginning")
d_queue.prepend("X")
d_queue.print_forward()
d_queue.print_backward()
print("\nDeleting element")
d_queue.delete("A")
d_queue.print_forward()
d_queue.print_backward()

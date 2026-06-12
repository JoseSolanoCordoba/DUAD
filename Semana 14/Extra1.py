class Node:
    data:str
    next:"Node"
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node  
    def __init__(self, head):
        self.head = head

    def print_structure(self):
        print("Imprimiendo estructura completa:")
        current_node = self.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next


class Queue(LinkedList):
    def dequeue(self):
        node_deleted = self.head
        self.head = self.head.next
        return node_deleted.data

    def enqueue(self, new_node):
        next_node = self.head         
        while (next_node is not None):
            current_node = next_node
            next_node = current_node.next
        new_node.next = None
        current_node.next = new_node
        return new_node.data


third_node = Node("C")
second_node = Node("B", third_node)
first_node = Node("A", second_node)

queue = Queue(first_node)
new_node = Node("D")

queue.print_structure()

print(f"Agregando un elemento: {queue.enqueue(new_node)}")

queue.print_structure()

print(f"Quitando un elemento: {queue.dequeue()}")

queue.print_structure()


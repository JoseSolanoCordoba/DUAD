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
        current_node = self.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next


class Stack(LinkedList):
    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        self.head = self.head.next

third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

stack = Stack(first_node)

print("Agregando un elemento")

stack.push(Node("Soy el nuevo nodo!"))
stack.print_structure()

print("Quitando un elemento")

stack.pop()
stack.print_structure()

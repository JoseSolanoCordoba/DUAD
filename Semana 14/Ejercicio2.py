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


class Double_Ended_Queue(LinkedList):
    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop_left(self):
        self.head = self.head.next

    def push_right(self, new_node):
        next_node = self.head.next         
        while (next_node is not None):
            current_node = next_node
            next_node = current_node.next
        new_node.next = None
        current_node.next = new_node

    def pop_right(self):
        current_node = self.head         
        next_node = self.head.next        
        while (next_node is not None):
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next
        previous_node.next = None

third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

double_queue = Double_Ended_Queue(first_node)
new_node = Node("Soy el nuevo nodo!")

print("Agregando un elemento a la izquierda")

double_queue.push_left(new_node)
double_queue.print_structure()

print("Quitando un elemento de la izquierda")

double_queue.pop_left()
double_queue.print_structure()

print("Quitando un elemento de la derecha")

double_queue.pop_right()
double_queue.print_structure()

print("Agregando un elemento a la derecha")

double_queue.push_right(new_node)
double_queue.print_structure()


class Node:
    data:str
    left_child:"Node"
    right_child:"Node"
    def __init__(self, data, left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class Binary_Tree():
    head: Node  
    def __init__(self, head):
        self.head = head
    def print_structure(self):
        self.print_node(self.head)

    def print_node(self, Node):
        if Node.left_child is not None:
            print(f'Parent ---> {Node.data}: Left_Child ---> {Node.left_child.data}\n') 
            self.print_node(Node.left_child)
        if Node.right_child is not None:
            print(f'Parent ---> {Node.data}: Right_Child ---> {Node.right_child.data}\n')
            self.print_node(Node.right_child)
        

seventh_node = Node("Soy el séptimo nodo")
sixth_node = Node("Soy el sexto nodo")
fifth_node = Node("Soy el quinto nodo")
fourth_node = Node("Soy el cuarto nodo")
third_node = Node("Soy el tercer nodo", sixth_node)
second_node = Node("Soy el segundo nodo", fourth_node, fifth_node)
first_node = Node("Soy el primer nodo", second_node, third_node)

tree = Binary_Tree(first_node)
tree.print_structure()

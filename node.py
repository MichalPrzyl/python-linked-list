class LinkedList:
    def __init__(self) -> None:
        self.first_node = None 
        self.last_node = None 

    def add_node(self, value):
        new_node = Node(value)
        self.last_node.next_node = new_node

class Node:
    value = None
    next_node = None

    def __init__(self, value) -> None:
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.first_node = None 
        self.last_node = None 

    def add_node(self, value):
        new_node = Node(value)

        # Settings first_node
        if not self.first_node:
            self.first_node = new_node

        # Settings last_node
        if self.last_node:
            self.last_node.next_node = new_node

        self.last_node = new_node

    def print_all_elements(self):
        current_node = self.first_node
        index_counter = 0

        # Main loop
        while True:
            print(f"{index_counter}. {current_node.value}")
            if not id(current_node) == id(self.last_node):
                current_node = current_node.next_node
                index_counter += 1
            else:
                break


class Node:
    def __init__(self, value) -> None:
        self.value = value


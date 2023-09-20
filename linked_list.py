class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    
    # Defining the equivalent append function from python lists
    def append(self, data):
        new_node = node(data)
        current_node = self.head

        # Traversing the list until last node
        while current_node.next != None:
            current_node = current_node.next
        
        # Setting the new node
        current_node.next = new_node

    # Function that returns the number of nodes
    @property
    def length(self):
        current_node = self.head
        total = 0

        while current_node.next != None:
            total += 1
            current_node = current_node.next

        return total

    # Method that print the data in the nodes of the linked list
    def display(self):
        elems = []
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)

        print(elems)

    def get(self, index):
        if index >= self.length:
            print("ERROR: 'get' Index out of range!")
            return None
        
        current_index = 0
        current_node = self.head

        while True:
            current_node = current_node.next
            if current_index == index: return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length:
            print("ERROR: 'get' Index out of range!")
            return None
        
        current_node = self.head
        current_index = 0

        while True:
            # We have to keep the last_node to maintain the proper order of the linked list
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


            


my_list = linked_list()

my_list.append(1)

my_list.append(2)

my_list.append(3)

my_list.append(4)

my_list.append(2)

my_list.display()
print(f"Length before erasing: {my_list.length}")
index = 3

my_list.erase(index)

my_list.display()

print(f"Length after erasing: {my_list.length}")



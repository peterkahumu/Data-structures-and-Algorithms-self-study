from typing import Any

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        """Provides a user friendly representation of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            if current == self.tail:
                break
            current = current.next

        return "->".join(elements) if elements else "The list is empty."
    
    def __repr__(self):
        return f"{self.__class__.__name__} (Size = {self.size}, elements = {self})"

    def is_empty(self):
        """Checks for absence of nodes in the list. Returns true if there's no node."""
        return self.head is None

    def prepend(self, data):
        """Adds a node at the beginning of the list."""
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
            self.tail.next = self.head
            self.increment_size()
            return
        
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.increment_size()
        return


    def append(self, data):
        """Insert data at the end of the list."""
        new_node = Node(data)

        if self.is_empty():
            self.prepend(data)
            return
        
        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node
        self.increment_size()
    
    def insert_at_index(self, index:int, data:Any):
        """Inserts a node at the specified index."""
        self.validate_index(index)
        if index > self.size:
            raise IndexError(f"Invalid index. The highest index you can provide is {self.size}")
        
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return
                
        new_node = Node(data)
        count = 0
        previous = None
        current = self.head
        while count < index:
            previous = current
            count += 1
            current = current.next

        previous.next = new_node
        new_node.next = current
        self.increment_size()
    
    def handle_delete_single_node(self):
        """Handles deletion when theres only one node in the  list."""        
        self.head = self.tail = None
        self.decrement_size()
        return
    
    def delete_first_node(self):
        """Removes the first elements of the list."""
        if self.is_empty():
            print("The list is empty.")
            return
        if self.head == self.tail:
           self.handle_delete_single_node()
           return      
        self.head = self.head.next
        self.tail.next = self.head
        self.decrement_size()
    
    def delete_last_node(self):
        """Remove the last node from the list."""
        if self.is_empty():
            print("The list is empty.")
            return
        if self.head == self.tail:
            # only one node is present.
            self.handle_delete_single_node()
            return
        
        current = self.head
        
        while current.next != self.tail:
            current = current.next

        current.next = self.head
        self.tail = current
        self.decrement_size()
    
    def delete_at_index(self, index:int):
        """Removes the node at the provided index"""
        self.validate_index(index)
        if self.is_empty():
            print("The list is empty.")
            return
        if index >= self.size:
            raise IndexError(f"The index provided is out of bound. The last element has an index of {self.size - 1}")
        
        if index == 0:
            self.delete_first_node()
            return

        if index == self.size - 1: # the last index
            self.delete_last_node()
            return
        
        current = self.head
        count = 0
        previous = None

        while count < index:
            previous = current
            current = current.next
            count += 1

        previous.next = current.next
        self.decrement_size()

    def search(self, data):
        if self.is_empty():
            print("The list is empty.")
            return
        
        current = self.head
        count = 0
        
        while current:
            if current.data == data:
                return count
            if current.next == self.head:
                break

            current = current.next
            count +=1
       
        return None # Data not found.

    def clear(self):
        self.head = self.tail = None
        self.size = 0
    
    def validate_index(self, index:int):
        if not isinstance(index, int):
            raise TypeError("The index must be an integer.")
        if index < 0:
            raise ValueError("The index must be a positive integer.")
        
    def increment_size(self):
        """Adds 1 to the current size value."""
        self.size += 1
        return
    
    def decrement_size(self):
        """Subracts 1 to the current size value"""
        if self.size == 0:
            return
        self.size -= 1
        return

    def display_list(self):
        """Returns a list of all the values in the linked list."""
        print(self)

my_list = CircularLinkedList()
my_list.append(10)
# my_list.delete_at_index(0)
my_list.prepend(5)
my_list.append(15)
my_list.insert_at_index(3, 0)
# my_list.delete_at_index(1)
# my_list.delete_last_node()
index = my_list.search(5)
if index != None:
    print("Data found at index ", index)
else:
    print("Data not found.")
print("The list has %d element(s)" %my_list.size)
print(my_list)
print(repr(my_list))
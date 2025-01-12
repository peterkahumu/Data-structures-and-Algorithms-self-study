class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        """Returns a user friendly representation of the list."""
        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next
        
        return "->".join(elements) if elements else  "The list is empty."  

    def __repr__(self):
        """Returns a brief explanation of the list."""
        return f"{self.__class__.__name__} (Size = {self.size}, Elements = {self})"

    def insert_at_beginning(self, data):
        """Inserts a node at the beginning of the list."""
        new_node  = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
            self.increment_size()
            return

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.increment_size()
    
    def insert_at_end(self, data):
        """Adds the provided data as the last element in the list.."""
        if self.is_empty():
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        self.increment_size()
    
    def insert_at_index(self, index:int, data):
        """Adds the provided data at the provided index.""" 
        if not self.validate_index(index, for_insertion=True):
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        if index == self.size:
            self.insert_at_end(data)
            return

        new_node = Node(data)        
        if index < self.size // 2: # index closer to head. Traverse forward
            current = self.head
            for _ in range(index):
                current = current.next
        else: # closer to tail
            current = self.tail
            for _ in range(self.size - index - 1):
                current = current.previous  

        previous = current.previous
        previous.next = new_node
        new_node.previous = previous
        new_node.next = current
        current.previous = new_node
        self.increment_size()

    def delete_first_node(self):
        """Deletes the first occurrence in the list (head)"""
        if self.is_empty():
            print("Empty list. Consider inserting nodes first.")
            return
        
        if self.head == self.tail: # only one node
            self.delete_loner_node("Cannot delete from an empty list.")
        next = self.head.next
        self.head.next = None
        next.previous = None
        self.head = next
        self.decrement_size()
        return

    def delete_last_node(self):
        """Deletes the last occurrence in the list (tail)"""
        if self.is_empty():
            print("Cannot delete in an empty list.")
            return

        if self.head == self.tail:
            self.delete_loner_node()
            return 
        
        previous = self.tail.previous
        self.tail.previous = None
        previous.next = None
        self.decrement_size()
        return
    
    def delete_at_index(self, index):
        """Delete the occurrence at the provided index."""
        if self.is_empty():
            print("Cannot delete in an empty list.")
            return
        
        if not self.validate_index(index):
            return

        if index == 0:
            self.delete_first_node()
            return
        
        if index == self.size -1 :
            self.delete_last_node()
            return
                
        if index < self.size // 2: # closer to head
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - index - 1):
                current = current.previous
        
        previous = current.previous
        next = current.next
        current.next = current.previous = None
        previous.next = next
        next.previous = previous
        self.decrement_size()
        return
    
    def delete_loner_node(self):
        """Handles deletion when only one node is present."""
        self.head = self.tail = None
        self.size = 0
        return
    
    def validate_index(self, index:int, for_insertion: bool = False):
        if not isinstance(index, int):
            raise TypeError("The index must be an integer.")
        if index < 0:
            raise ValueError("The index cannot be negative")
        
        if for_insertion:
            # validate the index for insertion purposes
            if index > self.size:
                raise IndexError(f"Index out of range. The largest index you can provide is {self.size}")
        else:
            if index >= self.size: # index range when deleting.
                raise IndexError(f"Index out of range. The largest index you can provide is {self.size - 1}")
        return True
    
    def search(self, data):
        if self.is_empty():
            print("Cannot search in an empty list.")
            return

        pointer1, pointer2 = self.head, self.tail
        start_index, end_index = 0, self.size -1    

        while pointer1 and pointer2 and start_index <= end_index: # ensure the pointer break on meeting or crossing
            if pointer1.data == data:
                print(f"{data} found at index", start_index)
                return
            if pointer2.data == data:
                print(f"{data} found at index ", end_index)
                return
            
            pointer1 = pointer1.next
            pointer2 = pointer2.previous
            start_index += 1
            end_index -= 1

        print(f"{data} not found")
        return
            
    def is_empty(self):
        """Returns True if the list is empty, otherwise, returns False."""
        return self.head is None
    
    def decrement_size(self):
        """Subtracts on from the size of the list when a node is removed."""
        if self.size == 0:
            self.size = 0
            return
        self.size -= 1

    def increment_size(self):
        """Adds 1 to the size of the list when a node is added."""
        self.size += 1
        return

    def clear(self):
        """Deletes all the elements of the list."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def display_list(self):
        """Displays all the data in the list."""
        print(self)


my_list = DoublyLinkedList()
my_list.insert_at_beginning(10)
my_list.insert_at_beginning(5)
my_list.insert_at_beginning(0)
my_list.insert_at_end(15)
my_list.insert_at_end(20)
my_list.insert_at_index(2, 9)
my_list.insert_at_index(4, 19)
my_list.insert_at_index(0, "Start")
my_list.insert_at_index(1, "List")
my_list.insert_at_index(my_list.size, 25) # Insert to be the last element in the list.
# my_list.delete_first_node()
# my_list.delete_last_node()
my_list.delete_at_index(3)
my_list.delete_at_index(7)
my_list.search(9)
my_list.search(15)
my_list.search(100)
my_list.display_list()
print(repr(my_list))
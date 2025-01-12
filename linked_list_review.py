class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        """Return a user friendly representation of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements) if elements else "Empty List."
    
    def __repr__(self):
        """Return a develper friendly represetation of a list."""
        return f"{self.__class__.__name__} (Size = {self.size}, elements = {str(self)})"
        
    
    def is_empty(self):
        """Checks if a list is empty and return true."""
        if not self.head:
            return True
        return False

    def increment_size(self):
        '''Increments the size by on on adding a node.'''
        self.size += 1
        return

    def decrement_size(self):
        '''Decrements the size by one on deleting a node.'''
        if self.size == 0: # avoid a negative number in the code.
            self.size = 0
            return
        self.size -= 1

    def prepend(self, data):
        '''Inserts data at the beginning of the linked list.'''
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail =  new_node           
        else:
            new_node.next = self.head
            self.head = new_node
        self.increment_size()
        return
        
    def append(self, data):
        '''Add an element to the end of the list.'''
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.increment_size()
        return        
        
    def insert_at_index(self, index:int, data):
        '''Inserts data at the provided index'''
        assert index >= 0, "Index cannot be negative" # raise an error of the user provides a negative number as index
        assert index <= self.size, f"Index out of range. Maximum index you can provide is {self.size}"

        if index == 0:
            self.prepend(data)
            return
        elif index == self.size:
            self.append(data)
            return
        else:
            new_node = Node(data)
            current = self.head
            previous = None
            count = 0

            while count < index:
                previous = current
                current = current.next
                count += 1

            previous.next = new_node
            new_node.next = current
            self.increment_size()
            return

    def delete_at_beginning(self):
        """Deletes the first element of the list."""
        if self.is_empty():
            print("The list is empty. Nothing to delete.")
            return
        elif not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.decrement_size()
    
    def delete_at_end(self):
        """Deletes the element at the end of the list."""
        if self.is_empty():
            print("Empty list. Cannot delete element.")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.decrement_size()
        else:            
            current = self.head
            while current.next != self.tail:
                current = current.next    

            current.next = None
            self.tail = current
            self.decrement_size()
    
    def delete_at_index(self, index:int):
        '''Deletes a node at a given index'''
        assert index < self.size, f"Index out of range. The last index is {self.size - 1}"
        assert index >= 0, "Index cannot be negative. Please use a valid index."

        if index == 0:
            self.delete_at_beginning()
            return
        elif index == self.size -1:
            self.delete_at_end()
            return
        else:
            current = self.head
            previous = None
            count = 0

            while count < index:
                previous = current
                current = current.next
                count += 1
            
            previous.next = current.next
            self.decrement_size()
        
    def remove_duplicates(self):
        """Removes any repititive elements in a list."""
        if self.is_empty():
            print("The list is empty.")
            return
        
        nodes = set()
        current = self.head
        previous = None

        while current:
            if current.data in nodes:
                previous.next =  current.next          
                if current == self.tail:
                    self.tail = previous
                self.decrement_size()
                return
            nodes.add(current.data)
            previous = current
            current = current.next
    
    def reverse_list(self):
        if self.is_empty():
            print("The list is empty")
        elif self.head == self.tail:
            return
        else:
            current = self.head
            previous = None
            
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            
            self.tail = self.head
            self.head = previous


    def search(self, data):
        if self.is_empty():
            print("The list is empty. Please insert values search.")
            return   
        count = 0
        current = self.head
        while current:
            if current.data == data:
                return count
            current = current.next
            count += 1

        return None

    def get_length(self):
        '''Returns the number of nodes in the list.'''
        return self.size
    
    def display_list(self):
        '''Displays all the nodes in the node if they are available.'''
        print(str(self))

        return
    
my_list = LinkedList()
my_list.prepend(0)
my_list.prepend(20)
my_list.prepend(30)
my_list.append(10)
my_list.append(50)
my_list.insert_at_index(3, 100)
my_list.insert_at_index(0, 0.00)
my_list.insert_at_index(6, 12)
my_list.insert_at_index(8, 150) 
# my_list.delete_at_beginning() # Deletes 0.0
# my_list.delete_at_beginning() # Deletes 30
# my_list.delete_at_end()
my_list.delete_at_index(2)
index = my_list.search(30)
if not index:
    print("Data not found")
else:
    print("Data found at index ", index)
my_list.remove_duplicates()
my_list.display_list()
my_list.reverse_list()
my_list.display_list()
print("The length of the list is now %d " %(my_list.size))
print(repr(my_list))
print(my_list.tail.data)

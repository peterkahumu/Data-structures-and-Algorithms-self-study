from typing import Any, Optional
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, value: Any) -> "None":
        '''Insert a node at the end of the list'''
        new_node = Node(value)
        if not self.head:
            self.prepend(value)
        else:
            tail = self.tail
            tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
            self.size += 1
        
    def prepend(self, value: Any) -> "None":
        '''Insert a  node at the beginning of the list'''
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            self.tail.next = self.head
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.size += 1

    def insertAtIndex(self, value: Any, index: Optional[int] = None) -> "None":
        '''Insert at a speciffied index. If one is not specified, default is at the beginning.'''
        if not index:
            self.prepend(value)
            return

        if index > self.size:
            raise ValueError("Index out of range. Maximum index is %d" %self.size)
              
        if index == self.size:
            self.append(value)
        else:
            new_node = Node(value)
            count = 0
            current = self.head
            
            while current and count != index:
                previous = current
                count += 1
                current = current.next
            
            previous.next = new_node
            new_node.next = current
            self.size += 1

    def deleteAtBeginning(self) -> "None":
        '''Deletes the first node of the linked list.'''
        if self.isEmpty():
            raise TypeError("Cannot delete at beginning: Empty list.")
        
        if self.head == self.tail: # only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1

    def deleteAtIndex(self, index: Optional[int] = None) -> "None":
        '''Deletes a node at a specified index. Deletes the first node if index in not provided.'''
        pass
    
    def deleteAtEnd(self) -> "None":
        '''Deletes the last node of the list.'''
        if self.isEmpty():
            raise TypeError("Cannot delete at end: Empty list.")
        
        if self.head == self.tail: # only one node in the list.
            self.head = None
            self.tail = None
        else:
            current = self.head
            
            while current.next != self.tail:
                current = current.next
            
            self.tail = current
            current.next = self.head
        self.size -= 1


    def find(self, value: Any) -> "int":
        '''Returns the index of the given value, else raises an error.'''
        pass

    def isEmpty(self) -> "bool":
        '''Return True if list has no values, else, False.'''
        return not self.head
    
    def getSize(self) -> "int":
        '''returns the number of nodes in a list'''
        return self.size
    
    def clear(self) -> "None":
        '''Deletes all nodes in the list.'''
        self.head = None
        self.tail = None
        self.size = 0
    
    def peek(self) -> Any:
        '''Returns the value of the first node first node.'''
        if self.isEmpty():
            raise TypeError("Cannot peek: Empty list.")
        
        return self.head.data
    
    def reverse(self) -> "None":
        '''Reverses the order of the list. '''
        pass

    def display_list(self) -> "None":
        '''Display all the values in the list.'''
        if self.isEmpty():
            raise TypeError("Empty list: Nothing to display.")
        
        if self.head == self.tail:
            print(self.head.data)
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                if current == self.tail:
                    break
                current = current.next
my_list = CircularlyLinkedList()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.prepend(-1)
my_list.insertAtIndex(-2)
my_list.insertAtIndex(6, 2)
# my_list.deleteAtBeginning()
my_list.deleteAtEnd()
print("The list has %d nodes." %my_list.getSize())
my_list.display_list()
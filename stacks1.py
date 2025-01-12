# class Stack:
#     def __init__(self):
#         self.data = []
    
#     def __str__(self):
#         return f"Stack({self.data})"
    
#     def push(self, data: int) -> "Stack":
#         '''Add items to the top of the stack.'''
#         self.data.append(data)
#         return self
    
#     def pop(self) -> "Stack":
#         '''Remove items at the top of the stack'''
#         if self.empty():
#             raise ValueError("Cannot pop: Empty stack")
#         return self.data.pop()
    
#     def print_stack(self) -> "Stack":
#         '''Print all the data in the stack.'''
#         print(self.data)
    
#     def empty(self) -> "Stack":
#         '''Returns True if there is no value in the stack.'''
#         return not self.data
    
#     def size(self)-> "Stack":
#         return len(self.data)
    
#     def peek(self) -> "Stack":
#         if self.empty():
#             raise TypeError("Cannot peek: Empty stack")
#         return self.data[-1]
    
# stack = Stack()
# stack.push(1).push(2).push(3).push(4)
# print("Is the stack empty: ", stack.empty())
# print(stack)
    
# from collections import deque
# from typing import Any

# class Stack:
#     '''Uses deques to implement the stack.'''
#     def __init__(self):
#         self.data = deque()

#     def size(self) -> "int":
#         '''Returns the number of elements in the stack.'''
#         return len(self.data)

#     def is_empty(self) -> "bool":
#         '''Returns True if the stack is empty, false if the stack has at least one value.'''
#         return not self.data
    
#     def push(self, value: Any) -> "None":
#         '''Add an element to the top of the stack.'''
#         return self.data.append(value)
        
    
#     def pop(self) -> "Any":
#         '''Remove the value at the top of the stack.'''
#         if self.is_empty():
#             raise TypeError("Cannot Pop: Empty stack.")
#         return self.data.pop()

#     def clear(self) -> "None":
#         '''Remove all the values from the stack'''
#         return self.data.clear()
    
#     def peek(self) -> "Any":
#         '''Return the value at the top of the stack.'''
#         if self.is_empty():
#             raise TypeError("Cannot peek: Empty stack")
#         return self.data[-1]

from typing import Any
class Node:
    '''Memory location to hold the pointer to the next node  and data.'''
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.size = 0

    def push(self, value: Any) -> "None":
        '''Add a node to the top of the stack.  (At the beginning)'''
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.size += 1
            return
        
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> "None":
        '''Get the last element added to the list, in this case the head'''
        if self.is_empty():
            raise TypeError("Cannot pop: Empty stack")
        self.head = self.head.next
        self.size -= 1
    
    def peek(self) -> "Any":
        '''Returns the value at the top of the stack'''
        if self.is_empty():
            raise TypeError("Cannot peek: Empty stack")
        return self.head.data

    def clear(self):
        '''Delete all values in the stack'''
        self.head = None
        # self.tail = None
        self.size = 0

    def is_empty(self):
        return not self.head

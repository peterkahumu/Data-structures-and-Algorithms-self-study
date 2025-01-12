from collections import deque

class Stack:
    def __init__(self):
        """Initializes an empty stack"""
        self._stack = deque()
    
    def __str__(self):
        """Returns a user-friendly string representation of the stack."""
        return str(self._stack)
    
    def __repr__(self):
        """Provided detailed information about the stack for debugging."""
        return f"{self.__class__.__name__}, (size = {self.size()}, elements = {self})"
    
    def size(self):
        """Returns the number of elements in the stack."""
        return len(self._stack)
    
    def empty(self):
        """Returns True if the stack is empty, else None"""
        return len(self._stack) == 0
    
    def pop(self):
        """Removes and returns the elememnt at the top of the stack."""
        if self.empty():
            raise IndexError("Popping from an empty stack.")        
        return self._stack.pop()
    
    def push(self, data):
        """Adds an element to the top of the stack."""
        return self._stack.append(data)
    
    def peek(self):
        """Returns the top most element of the stack without removing it."""
        return self._stack[-1]
    
    def clear(self):
        """Removes all the elements in the stack."""
        return self._stack.clear()
        
   
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("The topmost element in the stack is: ", stack.peek())
# stack.pop()
stack.clear()
print("Is the stack empty: ", stack.empty())
print(stack)
print(repr(stack))
from queue import LifoQueue

class Stack:
    def __init__(self):
        """Initializes an empty stack"""
        self._stack = LifoQueue(maxsize=10)

    def __str__(self):
        """Returns a user friendly string to the user."""
        return str(self._get_all_elements())
    
    def __repr__(self):
        """Returns a detailed Stack for developer."""
        return f"{self.__class__.__name__}, (size = {self.size()}, elements={self._get_all_elements()})"
    
    def size(self):
        """Returns the number of elements in the list."""
        return self._stack.qsize()
    
    def _get_all_elements(self):
        """Non-destructively retrieves all elements in the stack."""
        temp_list = []
        
        while not self._stack.empty():
            temp_list.append(self._stack.get())
        
        for element in reversed(temp_list):
            self._stack.put(element)
        return temp_list
    
    def put(self, data):
        self._stack.put(data)


stack = Stack()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack)
print(repr(stack))
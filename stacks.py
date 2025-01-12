class Stack:
    def __init__(self):
        """Initializes an empty stack."""
        self._stack = []

    def __str__(self):
        """Returns a user-friendly string representation of the stack."""
        return str(self._stack)

    def __repr__(self):
        """Returns a detailed representation of the stack for debugging."""
        return f"{self.__class__.__name__}, (size = {self.size()}, elements = {self._stack})"
        
    def empty(self):
        """Returns True if the stack is empty, otherwise False."""
        return len(self._stack) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self._stack)

    def push(self, data):
        """Pushes an element onto the top of the stack."""
        return self._stack.append(data)

    def pop(self):
        """Removes and returns the topmost element of the stack."""
        if not self.empty():
            return self._stack.pop()
        else:
            raise IndexError("Trying to pop from an empty stack.")

    def peek(self):
        """Returns the top most element of the stack without removing it."""
        if not self.empty():
            return self._stack[-1]
        else:
            raise IndexError("Peeking from an empty stack.")
        
    def clear(self):
        """Clears all the elements of the stack."""
        return self._stack.clear()


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print("The top element of the stack is: ", stack.peek())
print("The result of the peek: ", stack.peek())
print("The popping of the list now: ", stack.pop())
stack.clear()
print(stack)
print(repr(stack))
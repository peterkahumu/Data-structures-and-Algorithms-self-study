from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque()

    def __str__(self):
        """Return a user-friendly string."""
        return str(self._queue)
    
    def __repr__(self):
        """Returns detailed information to developers for debugging."""
        return f"{self.__class__.__name__}, (size = {self.size()}, elements = {self})"
    
    def size(self):
        """Returns the number of elements in the queue"""
        return len(self._queue)
    
    def is_empty(self):
        """Returns True if there are no elements in the queue, else False"""
        return self.size() == 0

    def enqueue(self, data):
        """Adds an element to the queue"""
        return self._queue.append(data)
    
    def queue_deque(self):
        """Removes the first element that was added to the queue. 
        
        :raises IndexError: if user tries to perform the operation on an empty queue."""
        return self._queue.popleft()
    
    def clear(self):
        """Destroys all the elements in the queue."""
        return self._queue.clear()
    
    def front(self):
        """Returns the first element in the queue."""
        return self._queue[0]
    
    def rear(self):
        """Returns the last element in the queue."""
        return self._queue[-1]
    
    
queue = Queue()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.queue_deque()
print(queue.front())
print(queue.rear())
# queue.clear()
print(queue)
print(repr(queue))
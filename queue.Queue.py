"""
- queue.Queue(maxsize) initializes a variable to a maximum size of maxsize.
maxsize 0 means an infinite loop.

Functions in the module are:
1. maxsize = Number of items allowed in the queue.
2. empty() = Return True if the queue is empty, False otherwise.
3. full() = Return True if there are maxsize items tin the queue, else False. If maxsize = 0, never returns True.
4. get() = Remove and return an item from the queue. If queue is empty, wait until an item is available.
5. get_nowait() - Return an item if one is immediately available, else Raise QueueEmpty.
6. put(item) - Put an item to the queue. If the queue is full, wait untill there is a free slot before adding the item.
7. put_nowait() - Put an item to the queue. If the queue is full, raise QueueFull.
qsize() - Returns the number of elements in the queue.
"""

from queue import Queue

class MyQueue:
    def __init__(self):
        self._queue = Queue()

    def __str__(self):
        """Return a user-friendly string representation of the queue."""
        elements = []
        while not self.empty():
            elements.append(str(self._queue.get()))

        return "->".join(elements) if elements else "Empty Queue."
    def __str__(self):
        """Return a detailed info of the queue"""
        return f"{self.__class__.__name__}, (size = {self.size()}, elements = {str(self)}"
    
    def empty(self):
        return self._queue.qsize() == 0

    def size(self):
        return self._queue.qsize()
    
    def enqueue(self, data):
        return self._queue.put(data)
    
    def deque(self):
        return self._queue.get_nowait()

    
    
queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(repr(queue))
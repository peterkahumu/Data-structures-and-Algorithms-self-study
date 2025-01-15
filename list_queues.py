class Queue:
    def __init__(self, maxsize = None):
        """Initializes an empty Queue with an optimal maximum size.
        :param maxsize: The maximums size of the queue (Default is None for unbounded queue.)
        """
        if maxsize is not None and maxsize < 0:
            raise ValueError("Maximum value must be a postive interger or None.")
        self.maxsize = maxsize
        self._queue = []

    def __str__(self):
        """Returns a User-Friendly representation of the Queue."""
        return " ".join(self._queue) if self._queue else "The Queue is empty."

    def __repr__(self):
        """Developer-friendly representation of the Queue."""
        return f"{self.__class__.__name__} (size = {self.size()}, maximum size = {self.maxsize}, elements = {self})"
    
    def size(self):
        """Returns the number of elements in the queue."""
        return len(self._queue)
    
    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self._queue) == 0
    
    def enqueue(self, data):
        """Adds an item to the queue
        :param data: The item to be added to the queue.
        :raises IndexError: If the Queue is full.
        """
        if self.maxsize is None or self.size() < self.maxsize:
            return self._queue.append(str(data))        
        raise IndexError(f"Queue of {self.maxsize} elements is full.")

    def dequeue(self):
        """Removes and returns the front item in the queue
        :return: The item at the front of the queue
        :raises IndexError: if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Error!! Trying to access values from an empty queue.")
        
        return self._queue.pop(0)

    def front(self):
        """Returns the front item from the queue.
        
        :return: Front Item

        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Error!! The queue is empty.")
        return self._queue[0]

    def rear(self):
        """Returns the last item from the queue without removing it.

        :return: Last Item.

        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Error!! The queue is empty.")
        return self._queue[-1]
    
    def print_queue(self):
        """Prints the elements of the stack  starting with the First to be entered."""
        print(self)
    
    def clear(self):
        """Destroys all elements of the queue and returns an empty queue."""
        self._queue.clear()
        return []

queue = Queue(maxsize=100)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
print("The first element in the queue is ", queue.front())
print("The last element in the queue is ", queue.rear())
print("Clearing all the elements in the queue ", queue.clear())
queue.print_queue()
print(repr(queue))
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # insert a value at the end of the list
    def append(self, data):
        '''Inserts the provided node at the end of the linked list.'''
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        tail = self.tail
        tail.next = new_node
        self.tail = new_node
        self.size += 1

    # insert a value at the beginning of the list
    def insertAtBeginning(self, data):
        '''Inserts the provided node at index 0'''
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        current = self.head
        new_node.next = current
        self.head = new_node
        self.size +=1

    # get the length of the list
    def length(self):
        '''Returns a count of all elements in the list'''
        # count = 0
        # current = self.head

        # while current:
        #     count += 1
        #     current = current.next
        
        # return count
        return self.size
    
    # get a given value given an index
    def get(self, index):
        try:
            '''Returns the value of the node at the index provided'''
            count = 0
            current = self.head
            if index >= self.size:
                print("Index out of range. Maximum index for the current list is {}".format(self.size - 1))
                return
            
            while count != index:
                current = current.next
                count +=1
            
            print("The data at index %d is %s" %(index, current.data))
        except Exception as e: 
            print("An error occured", e)
        

    # insert a value at a given index
    def insertAtIndex(self, index, data):
        try:
            '''Inserts data at the provided index'''
            current = self.head
            previous = None
            next = None
            count = 0
            new_node = Node(data)
            
            if index > self.size:
                print("Index out of range. Maximum index for the current list is {}".format(self.size - 1))
                return
            elif index == 0: # INSERT AT THE BEGINNING OF THE LIST
                self.insertAtBeginning(data)
                return
            elif index == self.size: # append a node.
                self.append(data)
                return
            else:
                while index != count and current.next: # one index behind
                    previous = current
                    next = current.next
                    count += 1
                    current = current.next

                previous.next = new_node
                new_node.next = next
            self.size += 1
        except Exception as e:
            print("An error occured, ", e)

    # delete a given value given the index
    def delete(self, index = 0):
        '''Deletes the first value(at index 0) by default if an index is not provided.'''
        try:
            if not self.head: # means the list is empty:
                print("The list is empty. Theres nothing to remove. ")
                return

            if index >=self.size:
                print("The index provided was out of range. The maximum index is ", self.size - 1)
                return

            current = self.head
            count = 0
            if index == 0:# delete the first element of the list, in this case, the head and reassign the head to the second value in the list.
                next = current.next
                self.head = next
                del(current)
                self.size -= 1
                return
            else:
                while index != count and current.next:
                    previous = current
                    count += 1
                    current = current.next
                
                previous.next = current.next
                del(current)
                self.size -=1
                
        except Exception as e:
            print("An error occured, ", e)

    # search if value exists and return the first index in case of duplicates.
    def search(self, data):
        '''Search for a given value and return the index'''
        if not self.head:
            print("Empty List. Please append or insert values first.")
            return
        
        if self.head.data == data:
            print("The data was found at index 0")
            return
        
        current = self.head
        index = 0
        while current:
            if current.data == data:
                print("The data was found at index %d " %index)
                return
            index +=1
            current = current.next
        print("Data provided not found. Please try again using another piece of data.")
        return
    
    def reverse_list(self):
        if not self.head:
            print("The list is empty.")
            return
        
        if not self.head.next: # only one node was present.
            return self.printList()

        current = self.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        self.head = previous
        print("\nReversed the list")
        return self.display()
    
    def swap_nodes(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        current = dummy_node

        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            

            first.next = second.next
            second.next = first
            current.next = second
            current = current.next.next

        self.head = dummy_node.next
        return self.display()

    # display all the data in the list.
    def display(self):
        current = self.head

        if not current:
            print("The list is empty. Please try appending some values")
            return

        while current:
            print(current.data, end=" ")
            current = current.next
        
        print()
        return
    
list = LinkedList()

list.append(2)
list.append(0)
list.append(4)
list.append(8)
list.append(4)
list.append(5)
list.append(6)
# list.insertAtBeginning(10)
# print ("The linked list has %d elements" %list.length())
# list.get(7)
# list.insertAtIndex(3, 30)
# list.insertAtIndex(8, 60)
# print ("The linked list now has %d elements" %list.length())
# #list.delete(8)
# list.search(2)
list.display()
print(list.tail.data)
# list.reverse_list()
# list.swap_nodes()
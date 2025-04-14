# Implement a Queue
# Create a class called Queue that implements a queue data structure. 
# The queue should support the following operations:
# enqueue(item): Adds an item to the back of the queue.
# dequeue(): Removes and returns the item from the front of the queue.
# peek(): Returns the item at the front of the queue without removing it.
# is_empty(): Returns True if the queue is empty and False otherwise.
# size(): Returns the number of items in the queue.
# Your Queue class should use only built-in Python tools, such as lists, 
# and should not use any external libraries or modules.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
# 1
print(queue.peek())
# 2
print(queue.size())
# 2
print(queue.is_empty())
# False
print(queue.dequeue())
# 2
print(queue.dequeue())
# 3
print(queue.dequeue())
# None
print(queue.is_empty())
# True
print(queue.size())
# 0
print(queue.peek())
# None
print(queue.dequeue())


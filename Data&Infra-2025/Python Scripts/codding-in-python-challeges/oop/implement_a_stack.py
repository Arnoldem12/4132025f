# Implement a Stack
# Create a class called Stack that implements a stack data structure.
# The stack should support the following operations:
# push(item): Pushes an item onto the top of the stack.
# pop(): Removes and returns the item at the top of the stack.
# peek(): Returns the item at the top of the stack without removing it.
# is_empty(): Returns True if the stack is empty and False otherwise.
# size(): Returns the number of items in the stack.
# Your Stack class should use only built-in Python tools, such as lists, 
# and should not use any external libraries or modules.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    # return len(self.stack) if self.stack else 0
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
# 3
print(stack.peek())
# 2
print(stack.is_empty()) 
# False
print(stack.size())
# 2
print(stack.pop())
# 2
print(stack.pop())
# 1
print(stack.pop())
# None
print(stack.is_empty())
# True
print(stack.size())
# 0
print(stack.pop())
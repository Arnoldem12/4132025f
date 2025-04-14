# Create a function called remove_duplicates that takes a list of elements as input and 
# returns a new list with duplicates removed. Your function should use only built-in Python tools and 
# should maintain the original order of elements while removing duplicates.

def remove_duplicates(lst):
    return list(dict.fromkeys(lst)) # dict.fromkeys() returns a dictionary with the specified keys and values.

                                 # The keys are unique, so duplicates are removed. The values are set to None.
                                     # The list() function converts the dictionary back to a list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_duplicates(lst))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# The function removes the duplicates from the list and returns a new list with the original order of elements.
# The function uses only built-in Python tools and should maintain the original order of elements while removing duplicates.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# Output: 55
# The function calculates the nth Fibonacci number using recursion. The function returns the nth Fibonacci number for the input value n.
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1.
# The function uses recursion to calculate the nth Fibonacci number by summing the previous two numbers in the sequence.
# The function returns the nth Fibonacci number for the input value n.


# Create a function called remove_duplicates that takes a list of elements as input 
# and returns a new list with duplicates removed. Your function should use only built-in Python tools 
# and should maintain the original order of elements while removing duplicates.

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
# dict.fromkeys() returns a dictionary with the specified keys and values.
    # The keys are unique, so duplicates are removed. The values are set to None.
    # The list() function converts the dictionary back to a list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_duplicates(lst))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# The function removes the duplicates from the list and returns a new list with the original order of elements.
# The function uses only built-in Python tools and should maintain the original order of elements while removing duplicates.


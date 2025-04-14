# Find Common Elements in Two Lists
# Create a function called find_common_elements that takes two lists of integers 
# as input and returns a list containing the common elements between the two input lists. 
# The order of elements in the resulting list does not matter. 
# Your function should use only built-in Python tools.

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Test Cases
list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7, 8]
print(find_common_elements(list1, list2))  # Output: [4, 5]
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8]
print(find_common_elements(list1, list2))  # Output: [5]
# Merge Sorted Lists
# Create a function called merge_sorted_lists that takes two sorted lists of integers as input 
# and returns a single sorted list containing all the elements from both input lists. 
# Your function should use only built-in Python tools.

# In: ([1, 3, 5], [2, 4, 6])
# Out: [1, 2, 3, 4, 5, 6]
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
# [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))
# [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([], [1, 2, 3]))
# [1, 2, 3]
print(merge_sorted_lists([1, 2, 3], []))
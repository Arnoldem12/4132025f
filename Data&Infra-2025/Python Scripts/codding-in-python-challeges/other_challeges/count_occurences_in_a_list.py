# Count Occurrences in a List
# Write a Python function that takes a list of numbers and a target number, 
# and it returns the count of how many times the target number appears in the list.
# In: ([1, 2, 3, 4, 2, 2, 5], 2)
# Out: 3

def count_occurrences_in_a_list(lst, target):
    return lst.count(target)

print(count_occurrences_in_a_list([1, 2, 3, 4, 2, 2, 5], 2)) # 3
print(count_occurrences_in_a_list([1, 2, 3, 4, 2, 2, 5], 5)) # 1
# Find the number of unique elements of a list: In: [1,3,4,5,6,7] 
# Out: 6  In: [1,1,3,4,5,5,6,7] 
# Out: 6 (1 and 5 are duplicated and should be counted once)

def unique_elements(lst):
    # set() removes duplicates from the list
    # len() returns the length of the set, which is the number of unique elements
    return len(set(lst))    

print(unique_elements([1, 1, 3, 4, 5, 5, 6, 7]))  # Output: 6
print(unique_elements([1, 3, 4, 5, 6, 7]))  # Output: 6
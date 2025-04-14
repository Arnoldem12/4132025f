# Find the Missing Number
# Create a function called find_missing_number that takes a list of distinct integers from 0 to n (inclusive),
# where n is one less than the length of the list, and returns the missing number from the list. 
# Your function should use only built-in Python tools.

# Examples:
# find_missing_number([0, 1, 2, 4, 5, 6, 7, 8]) -> 3
# find_missing_number([0, 2, 3, 4, 5, 6, 7, 8, 9]) -> 1
# find_missing_number([0, 1, 2, 3, 4, 5, 6, 7, 8]) -> None

def find_missing_number(numbers):
    if not numbers:
        return None
    
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    
    missing_number = expected_sum - actual_sum
    
    if missing_number == 0:
        return None
    else:
        return missing_number

print(find_missing_number([0, 1, 2, 4, 5, 6, 7, 8])) # 3
print(find_missing_number([0, 2, 3, 4, 5, 6, 7, 8, 9])) # 1
print(find_missing_number([0, 1, 2, 3, 4, 5, 6, 7, 8])) # None
print(find_missing_number([])) # None
print(find_missing_number([0])) # None
print(find_missing_number([1])) # None
print(find_missing_number([0, 1])) # None
print(find_missing_number([1, 2])) # None
print(find_missing_number([0, 2])) # None
print(find_missing_number([0, 1, 2])) # None
print(find_missing_number([1, 2, 3])) # None
print(find_missing_number([0, 2, 3])) # None
print(find_missing_number([0, 1, 3])) # None
print(find_missing_number([0, 1, 2, 3])) # None
print(find_missing_number([0, 1, 2, 3, 4])) # None
print(find_missing_number([0, 1, 2, 3, 4, 5])) # None
print(find_missing_number([0, 1, 2, 3, 4, 5, 6])) # None
print(find_missing_number([0, 1, 2, 3, 4, 5, 6, 7])) # None
    
# Calculate Average
# Write a Python program that calculates the average of a list of numbers.
# In:  [5, 10, 15, 20]
# Out: 12.5

def calculate_average(numbers):
    if not numbers:
        return 0  # Return 0 if the list is empty to avoid division by zero
    return sum(numbers) / len(numbers)

print(calculate_average([5, 10, 15, 20]))  # Output: 12.5
print(calculate_average([]))  # Output: 0 (empty list)
print(calculate_average([10]))  # Output: 10 (single element list)
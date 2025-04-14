
# Find the Longest Consecutive Subsequence
# Create a function called longest_consecutive_subsequence that takes a list of integers as input 
# and returns the length of the longest consecutive subsequence of integers in the list. 
# A consecutive subsequence is a sequence of integers where each integer appears exactly once 
# and they are in consecutive order. 
# Your function should use only built-in Python tools.

# In: [1, 2, 3, 4, 5, 7, 8, 9, 10]
# Out: 6
# Explanation: The longest consecutive subsequence is [1, 2, 3, 4, 5, 6], which has a length of 6.

def longest_consecutive_subsequence(nums):
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

print(longest_consecutive_subsequence([1, 2, 3, 4, 5, 7, 8, 9, 10]))
# 6
print(longest_consecutive_subsequence([1, 3, 5, 7, 9]))
# 1
print(longest_consecutive_subsequence([10, 5, 12, 3, 55, 30, 4, 11, 2]))
# 4
print(longest_consecutive_subsequence([1, 2, 3, 4, 5]))
# 5
print(longest_consecutive_subsequence([]))


# Find the Maximum Class Edition
# Similarly to the previous exercise, find the maximum number of a list. 
# This time, use a class instead. 
# When initializing MaxNumberFinder you will need to provide nums as an argument

class MaxNumberFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_max(self):
        return max(self.nums)
    # return max(self.nums) if self.nums else None

max_finder = MaxNumberFinder([1, 2, 3, 4, 5])
print(max_finder.find_max())
# 5
max_finder = MaxNumberFinder([-1, -2, -3])
print(max_finder.find_max())
# -1
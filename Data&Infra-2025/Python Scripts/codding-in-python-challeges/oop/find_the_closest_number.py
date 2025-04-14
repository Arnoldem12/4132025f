
# Find The Closest Number
# Write a function that finds the first closest number in a list
# In: ([2, 4, 8, 10], 6)
# Out: 4

class ClosestNumberFinder:  
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_closest(self):
        return min(self.nums, key=lambda x: abs(x - self.target))
    
closest_finder = ClosestNumberFinder([2, 4, 8, 10], 6)
print(closest_finder.find_closest())
# 4
closest_finder = ClosestNumberFinder([2, 4, 8, 10], 5)
print(closest_finder.find_closest())
# 4
closest_finder = ClosestNumberFinder([2, 4, 8, 10], 7)
print(closest_finder.find_closest())
# 8
#Find the Maximum Number in a List Description: Write a function 
#that takes a list of numbers as input and returns the maximum 
#number in the list. Input: [5, 9, 2, 12, 7] Output: 12

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [5, 9, 2, 12, 7]
max_number = find_max(numbers)
print("The maximum number in the list is:", max_number)

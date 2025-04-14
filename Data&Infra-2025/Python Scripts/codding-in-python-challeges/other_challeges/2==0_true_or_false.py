#Write a function called is_even that takes a number as an argument 
#and returns True if it's even, and False otherwise
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False

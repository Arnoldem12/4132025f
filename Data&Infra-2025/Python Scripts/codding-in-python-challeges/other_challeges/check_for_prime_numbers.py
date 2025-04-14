# Check for Prime Numbers
# Create a function called is_prime that takes an integer as input 
# and returns True if the number is prime and False otherwise. 
# Your function should use only built-in Python tools.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
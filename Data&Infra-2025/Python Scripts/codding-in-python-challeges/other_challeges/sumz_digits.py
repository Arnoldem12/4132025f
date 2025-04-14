# Calculate Sum of Digits
# Write a function called sum_of_digits that takes a positive integer as an argument and 
# returns the sum of its digits. For example, the input 1234 should return 10, which is the sum of 1, 2, 3, and 4.

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

print(sum_of_digits(1234))
# Output: 10
# The function calculates the sum of digits for the input integer n.
# The function uses a while loop to iterate through the digits of the number.
# The function extracts the last digit of the number using the modulus operator % and adds it to the total.
# The function divides the number by 10 using integer division // to remove the last digit.
# The function continues this process until the number becomes 0.
# The function returns the total sum of digits for the input integer n.
# The function uses a while loop to iterate through the digits of the number.
# The function extracts the last digit of the number using the modulus operator % and adds it to the total.
# The function divides the number by 10 using integer division // to remove the last digit.
# The function continues this process until the number becomes 0.
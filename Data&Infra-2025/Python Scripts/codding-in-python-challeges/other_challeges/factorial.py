#Write a function called 
#factorial that takes a positive 
#integer as an argument and returns its factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

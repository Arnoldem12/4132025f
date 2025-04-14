# Fibonacci Series
# Write a program that generates the Fibonacci series up to a given number 'n'.
# fibonacci(0) -> []
# fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
# fibonacci(23) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while fib[-1] + fib[-2] < n:
            fib.append(fib[-1] + fib[-2])
        return fib
 
print(fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(23)) # [0, 1, 1, 2, 3, 5, 8, 13, 21]
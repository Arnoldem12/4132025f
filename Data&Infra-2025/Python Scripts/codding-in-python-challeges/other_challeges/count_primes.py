# Count Primes
# Description: Write a function that takes an integer n as input and 
# returns the count of prime numbers less than n. Input: 10 Output: 4 (Primes less than 10: 2, 3, 5, 7)

def count_primes(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)

print(count_primes(10)) # 4
print(count_primes(20)) # 8
print(count_primes(100)) # 25

"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""


def is_prime(n: int) -> bool:
    if n <= 1:
        return False  # constraint that n>=0
    ii = 2
    while ii * ii <= n:
        if n % ii == 0:
            return False
        ii += 1
    return True


def count_primes(n: int) -> int:
    count = 0
    for ii in range(1, n):
        if is_prime(ii):
            count += 1

    return count


print(count_primes(15))

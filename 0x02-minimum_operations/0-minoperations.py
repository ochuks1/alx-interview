#!/usr/bin/python3
"""
Calculates the minimum operations to reach exactly n H characters.

Prototype: def minOperations(n)
Returns an integer.
If n is impossible to achieve, return 0.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to achieve n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum operations needed; 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1
    return operations

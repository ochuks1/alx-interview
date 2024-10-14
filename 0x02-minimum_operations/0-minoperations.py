#!/usr/bin/python3


def minOperations(n):
    """
    Calculates the minimum number of operations to achieve n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum operations needed; 0 if impossible.
    """
    if n <= 1:
        return 0  # If n is 1 or less, no operations needed

    operations = 0
    factor = 2  # Start checking for factors from 2

    while n > 1:
        if n % factor == 0:  # If factor is a divisor of n
            operations += factor  # Add the factor to operations count
            n //= factor  # Reduce n
        else:
            factor += 1  # Check the next factor

    return operations


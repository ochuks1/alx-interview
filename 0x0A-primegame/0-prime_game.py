#!/usr/bin/python3
"""
Prime Game: Determine the winner of multiple rounds of the game.
"""

def is_prime(n):
    """Check if a number is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_counts(n):
    """
    Generate a list where each index represents the count of primes from 1 to that index.
    """
    prime_counts = [0] * (n + 1)
    for i in range(2, n + 1):
        prime_counts[i] = prime_counts[i - 1]
        if is_prime(i):
            prime_counts[i] += 1
    return prime_counts

def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): Array of integers representing the maximum number for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    prime_counts = generate_prime_counts(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Maria wins if the count of primes up to n is odd
        # Ben wins if it's even
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

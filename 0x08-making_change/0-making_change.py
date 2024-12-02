#!/usr/bin/python3
"""
This module provides a function to solve the coin change problem.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    
    Args:
        coins (list): A list of integers representing the denominations of coins.
        total (int): The total amount to reach using the coins.

    Returns:
        int: The minimum number of coins needed to reach the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for a greedy approach
    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        if total == 0:
            break
        num_coins = total // coin
        coin_count += num_coins
        total -= num_coins * coin

    return coin_count if total == 0 else -1

#!/usr/bin/python3
"""
Coin Change Module

This module provides a function `makeChange` to determine the minimum number
of coins required to make up a given total amount, using the provided
coin denominations.

The function supports:
- Greedy algorithm for quick solutions.
- Dynamic programming for correctness with arbitrary denominations.

Typical Use Cases:
- Calculating change for vending machines.
- Solving optimization problems related to currency denominations.
- Algorithmic challenges involving greedy or dynamic programming approaches.

"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of integers representing the denominations
        of coins available.
        total (int): The total amount for which change is required.

    Returns:
        int: The minimum number of coins needed to make up the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins for total 0

    # Compute minimum coins for each amount up to total
    for amount in range(1, total + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

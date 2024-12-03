#!/usr/bin/python3
def makeChange(coins, total):
    """Determines the fewest number of coins needed to make up a given total."""
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

#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    If total is 0 or less, return 0 since no coins are needed
    """
    if total <= 0:
        return 0

    # Create an array to store the minimum number of coins required to reach each value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Update the minimum number of coins required for each value
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the minimum number of coins required to reach the total value
    return min_coins[total] if min_coins[total] != float('inf') else -1

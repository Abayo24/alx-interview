#!/usr/bin/python3
"""
determines who the winner of each game is.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    """
    if not nums or x < 1:
        return None

        max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes = [i for i in range(2, max_n + 1) if sieve[i]]

    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + sieve[i]

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

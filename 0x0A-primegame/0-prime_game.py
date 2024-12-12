#!/usr/bin/python3
"""
Prime Game module
"""


def sieve_of_eratosthenes(max_num):
    """
    Generate a list of primes up to max_num using the Sieve of Eratosthenes.
    """
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        turn = 0  # 0 for Maria, 1 for Ben

        while primes_in_game:
            turn += 1
            prime = primes_in_game.pop(0)
            primes_in_game = [p for p in primes_in_game if p % prime != 0]

        if turn % 2 == 1:  # Maria wins
            wins["Maria"] += 1
        else:  # Ben wins
            wins["Ben"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    return None

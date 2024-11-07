#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Calculates the minimum number of operations to reach exactly n H characters.'''
    if n <= 1:
        return 0

    ops_count = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            ops_count += divisor
            n //= divisor
        divisor += 1

    return ops_count

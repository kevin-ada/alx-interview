#!/usr/bin/python3

"""The Prime"""


def isWinner(x, nums):
    """The Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, p in enumerate(primes) if p]
    primes = primes[1:]
    c = 0
    for i in nums:
        if i in primes:
            c += 1
        if c == x:
            return "Maria"
    return "Ben"
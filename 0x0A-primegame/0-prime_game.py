#!/usr/bin/python3

"""The Prime"""


def isWinner(x, nums):
    """The Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [False, False] + [True for i in range(n - 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, prime in enumerate(primes) if prime]
    m = len(primes)
    scores = [0, 0]
    for i in range(1, m + 1):
        scores[0] += 1
        if i == m or primes[i] > n:
            break
    for i in range(1, m + 1):
        scores[1] += 1
        if i == m or primes[i] > n:
            break
    if scores[0] == scores[1]:
        return None
    return "Ben" if scores[0] > scores[1] else "Maria"

#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file."""
    if not isinstance(n, int):
        return 0
    ops = 0
    clip = 0
    happened = 1
    while happened < n:
        if clip == 0:
            clip = happened
            happened += clip
            ops += 2
        elif n - happened > 0 and (n - happened) % happened == 0:
            clip = happened
            happened += clip
            ops += 2
        elif clip > 0:
            happened += clip
            ops += 1
    return ops

#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed
    to meet a given amount total"""
    if total <= 0:
        return 0
    remind = total
    coin_needed = 0
    coin_indexes = 0
    coins_sorted = sorted(coins, reverse=True)
    listlen = len(coins)
    while remind > 0:
        if coin_indexes >= listlen:
            return -1
        if remind - coins_sorted[coin_indexes] >= 0:
            remind -= coins_sorted[coin_indexes]
            coin_needed += 1
        else:
            coin_indexes += 1
    return coin_needed

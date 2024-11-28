#!/usr/bin/python3
"""
0-making_change.py
"""


def makeChange(coins, total):
    """
    Returns fewest number of coins needed to give a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= temp * coin
    if total != 0:
        return -1
    return change

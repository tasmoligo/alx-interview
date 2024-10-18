#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in
    exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    count_H = 1
    ops = 0
    while count_H < n:
        if n % count_H == 0:
            ops *= 2
            count_H += 1
        else:
            remaining = n - count_H
            ops += remaining
            break
    return ops


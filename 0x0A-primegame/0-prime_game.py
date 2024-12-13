#!/usr/bin/python3
"""
0-prime_game.py
"""


def isWinner(x, nums):
    """
    Determines the winner of the game.
    """

    if not nums or x < 1:
        return None
    maxNum = max(nums)

    sortRange = [True for _ in range(max(maxNum + 1, 2))]
    for i in range(2, int(pow(maxNum, 0.5)) + 1):
        if not sortRange[i]:
            continue
        for j in range(i * i, maxNum + 1, i):
            sortRange[j] = False
    sortRange[0] = sortRange[1] = False
    y = 0
    for i in range(len(sortRange)):
        if sortRange[i]:
            y += 1
        sortRange[i] = y
    player1 = 0
    for x in nums:
        player1 += sortRange[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"

#!/usr/bin/python3
"""
Program to place N non-attacking queens on an N×N chessboard
"""

import sys


def solutionFunc(row, col):
    solution = [[]]
    for queen in range(row):
        solution = setQueen(queen, col, solution)
    return solution


def setQueen(queen, col, solution):
    """
    Sets the queen on the board
    """
    position = []
    for arg in solution:
        for x in range(col):
            if safe(queen, x, arg):
                position.append(arg + [x])
    return position


def safe(queen, x, arg):
    """
    Makes sure there is no repetition
    """
    if x in arg:
        return False
    else:
        return all(abs(arg[col] - x) != queen - col
                   for col in range(queen))


def safeplay():
    """
    Checks for command line arguments
    """
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    N = sys.argv[1]
    if not N.isdigit():
        print('N must be a number')
        sys.exit(1)
    else:
        N = int(N)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)
    return N


def nqueen():
    """
    The main program
    """
    n = safeplay()
    solution = solutionFunc(n, n)
    for arg in solution:
        position = []
        for queen, num in enumerate(arg):
            position.append([queen, num])
        print(position)


if __name__ == "__main__":
    nqueen()

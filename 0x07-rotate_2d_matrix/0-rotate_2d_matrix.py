#!/usr/bin/python3
"""
0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            a = matrix[i][j]
            b = matrix[j][i]
            a, b = b, a
    for i in range(n):
        matrix[i].reverse()

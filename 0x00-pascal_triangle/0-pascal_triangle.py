#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
        the Pascal’s triangle of n:

    - Returns an empty list if n <= 0
    - You can assume n will be always an integer
    """
    triangleList = []
    if n <= 0:
        return triangleList
    for i in range(n):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(triangleList[i - 1][j-1] + triangleList[i-1][j])
        triangleList.append(temp)
    return triangleList

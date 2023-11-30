#!/usr/bin/python3
"""Define a function to print the pascal triangle"""


def pascal_triangle(n):
    """Implements the function of pascal triangle"""
    if n <= 0:
        return []
    lists = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    lists[i].append(1)
                else:
                    lists[i].append(lists[i - 1][j] + lists[i - 1][j - 1])
            elif (j == i):
                    lists[i].append(1)
    return lists

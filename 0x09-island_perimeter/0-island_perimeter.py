#!/usr/bin/python3
"""
Module defining a function which provides
a solution to the island_perimeter problem
"""
from typing import List


def island_perimeter(grid: List[List[int]]):
    """
    Function which provides
    a solution to the island_perimeter problem
    """
    perimeter = 0

    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if (grid[i][j] == 1):
                perimeter += 4
            j += 1
        i += 1

    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if (grid[i][j] == 1):
                if (i > 0 and grid[i - 1][j] == 1):
                    perimeter -= 2
                if (j > 0 and grid[i][j - 1] == 1):
                    perimeter -= 2
            j += 1
        i += 1

    return perimeter

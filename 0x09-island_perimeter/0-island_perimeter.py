#!/usr/bin/python3
"""
Island Perimeter Module

This module defines the function `island_perimeter` to calculate the perimeter
of an island described in a grid. The grid is a list of lists of
integers where:
- 0 represents water.
- 1 represents land.
- Each cell is square with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with no lakes (water completely surrounded by land).

Example:
    >>> grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    >>> island_perimeter(grid)
    12
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A 2D grid representing
        water (0) and land (1).

    Returns:
        int: The perimeter of the island.

    Algorithm:
        - Iterate through each cell in the grid.
        - If the cell is land (1), add 4 to the perimeter.
        - Subtract 2 for each adjacent land cell to avoid double counting.

    Example:
        >>> grid = [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0]
        ]
        >>> island_perimeter(grid)
        8
    """
    if not grid or not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Found land
                # Add 4 for the current land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:  # Check top neighbor
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check left neighbor
                    perimeter -= 2

    return perimeter

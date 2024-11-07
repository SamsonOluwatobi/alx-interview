#!/usr/bin/python3
"""N queens solution finder module."""


import sys

def get_input():
    """Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(queen1, queen2):
    """Checks if two queens are attacking each other."""
    return (queen1[0] == queen2[0] or  # same row
            queen1[1] == queen2[1] or  # same column
            abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]))  # samediagonal

def solve_n_queens(n):
    """Finds all solutions for the N queens problem.

    Args:
        n (int): The size of the chessboard.

    Returns:
        List of solutions, each solution is a list of positions.
    """
    solutions = []
    def backtrack(row, queens):
        if row == n:
            solutions.append([queen.copy() for queen in queens])
            return
        for col in range(n):
            new_queen = [row, col]
            if all(not is_attacking(new_queen, q) for q in queens):
                queens.append(new_queen)
                backtrack(row + 1, queens)
                queens.pop()

    backtrack(0, [])
    return solutions

# Get input and solve
n = get_input()
solutions = solve_n_queens(n)
for solution in solutions:
    print(solution)

#!/bin/usr/python3
"""
    0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        Matrix (list of list of int): The n x n matrix to rotate.
    """
    n = len(matrix)

    # Transpose the matrix (swap rows and colums).
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()

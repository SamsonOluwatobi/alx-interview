#!/usr/bin/python3
'''A module for generating Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    Pascal's triangle of a given integer `n`.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists where each sublist represents a row in Pascal's triangle.
    '''
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle
    
    for i in range(n):
        row = []
        for j in range(i + 1):
            # First and last elements in each row are 1
            if j == 0 or j == i:
                row.append(1)
            else:
                # Each element is the sum of two elements directly above it
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    
    return triangle

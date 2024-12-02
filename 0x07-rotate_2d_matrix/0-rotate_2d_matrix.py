#!/usr/bin/python3
"""
This module contains a function to rotate
a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.
    Args:
        matrix (list[list[int]]): The n x n 2D matrix to rotate.
    """
    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree rotation
    for row in matrix:
        row.reverse()

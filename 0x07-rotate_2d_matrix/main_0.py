#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    # Test case 1
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print("Before rotation:")
    print(matrix)
    rotate_2d_matrix(matrix)
    print("After rotation:")
    print(matrix)

    # Test case 2
    matrix = [[1, 11, 13, 19],
              [41, 32, 6, 22],
              [55, 21, 41, 66],
              [77, 29, 78, 2]]
    print("Before rotation:")
    print(matrix)
    rotate_2d_matrix(matrix)
    print("After rotation:")
    print(matrix)

    # Test case 3
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    print("Before rotation:")
    print(matrix)
    rotate_2d_matrix(matrix)
    print("After rotation:")
    print(matrix)

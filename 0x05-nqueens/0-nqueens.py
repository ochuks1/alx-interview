#!/usr/bin/python3
"""
N Queens Problem Solver
Solves the N-Queens problem for a given N (>=4)
"""

import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe"""
    # Check column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solves the N Queens problem and prints each solution"""
    def place_queen(board, row):
        if row == n:
            # Print the solution as a list of [row, col]
            print([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                place_queen(board, row + 1)

    board = [-1] * n
    place_queen(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

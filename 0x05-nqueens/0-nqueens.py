#!/usr/bin/python3
import sys


def print_solution(board):
    """ Prints one solution in the required format """
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)


def is_safe(board, row, col):
    """ Check if placing a queen at (row, col) is safe """
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True


def solve_nqueens(board, col, N):
    """ Recursively solve the N Queens problem """
    if col == N:
        print_solution(board)
        return

    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row
            solve_nqueens(board, col + 1, N)


def nqueens(N):
    """ Main function to solve N Queens """
    board = [-1] * N
    solve_nqueens(board, 0, N)


def main():
    """ Main entry point of the program """
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

    nqueens(N)


if __name__ == "__main__":
    main()

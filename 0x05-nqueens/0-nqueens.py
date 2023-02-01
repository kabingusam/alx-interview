#!/usr/bin/python3
'''
A program that solves the N queens problem
'''
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end = " ")
        print()

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False

def n_queens(n):
    board = [[0 for i in range(n)] for j in range(n)]

    if solve_n_queens(board, 0) == False:
        print("Solution does not exist")
        return False

    print_board(board)
    return True

# Driver code
n = int(input("Enter number of queens: "))
n_queens(n)

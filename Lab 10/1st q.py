import numpy as np

board = np.zeros((8, 8), dtype=int)

def is_safe(board, row, col):
    if 1 in board[:row, col]:
        return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i, j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
        if board[i, j] == 1:
            return False
    return True

def solve(board, row=0):
    if row == 8:
        return True
    for col in range(8):
        if is_safe(board, row, col):
            board[row, col] = 1
            if solve(board, row + 1):
                return True
            board[row, col] = 0
    return False

solve(board)
print(board)
import random
import time
import os

initial = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
terminal = [[1, 2, 3], [4, 5, 6], [-1, 7, 8]]

def print_board(board, prompt):
    os.system('clear')
    print(prompt)
    for row in board:
        print(row)
    time.sleep(0.5)


def getPointer(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == -1:
                return (i, j)

def swap(board, i, j, k, l):
    temp = board[i][j]
    board[i][j] = board[k][l]
    board[k][l] = temp

def search(board, n):
    pointer = getPointer(board)
    if board == terminal:
        return n

    if n > 10:
        return -1

    if pointer[0] - 1 >= 0:
        swap(board, pointer[0] - 1, pointer[1], pointer[0], pointer[1])
        print_board(board, n)
        ret = search(board, n + 1)
        if ret != -1:
            swap(board, pointer[0] - 1, pointer[1], pointer[0], pointer[1])
    if pointer[0] + 1 < len(board):
        swap(board, pointer[0] + 1, pointer[1], pointer[0], pointer[1])
        print_board(board, n)
        ret = search(board, n + 1)
        if ret != -1:
            swap(board, pointer[0] + 1, pointer[1], pointer[0], pointer[1])
    if pointer[1] + 1 < len(board[0]):
        swap(board, pointer[0], pointer[1] + 1, pointer[0], pointer[1])
        print_board(board, n)
        ret = search(board, n + 1)
        if ret != -1:
            swap(board, pointer[0], pointer[1] + 1, pointer[0], pointer[1])
    if pointer[1] - 1 >= 0:
        swap(board, pointer[0], pointer[1] - 1, pointer[0], pointer[1])
        print_board(board, n)
        ret = search(board, n + 1)
        if ret != -1:
            swap(board, pointer[0], pointer[1] - 1, pointer[0], pointer[1])

moves = search(initial, 0)

print('moves =', moves)
import random
import time
import os
import copy

class PuzzleBoard:
    def __init__(self):
        self.board = self.generate_solved_board()
        self.empty_tile = (2, 2)
        self.shuffle_board()
        self.original = copy.deepcopy(self.board.copy())
        self.ATTEMPS = 0
        self.memory = []
        self.solved_at = 99999
        self.solution = []

    def generate_solved_board(self):
        return [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def shuffle_board(self):
        self.board = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
        # moves = ['up', 'down', 'left', 'right']
        # for _ in range(100):
        #     move = random.choice(moves)
        #     self.move_tile(move)

    def print_board(self):
        os.system('clear')
        print(f"Attemps: {self.ATTEMPS}")
        print(f"Memory: {self.memory}")
        for row in self.board:
            print(' '.join(str(tile) if tile != 0 else ' ' for tile in row))
        print()
        time.sleep(0)


    def print_original(self):
        for row in self.original:
            print(' '.join(str(tile) if tile != 0 else ' ' for tile in row))
        print()

    def move_tile(self, direction):
        x, y = self.empty_tile
        if direction == 'up' and x > 0:
            self.board[x][y], self.board[x-1][y] = self.board[x-1][y], self.board[x][y]
            self.empty_tile = (x-1, y)
        elif direction == 'down' and x < 2:
            self.board[x][y], self.board[x+1][y] = self.board[x+1][y], self.board[x][y]
            self.empty_tile = (x+1, y)
        elif direction == 'left' and y > 0:
            self.board[x][y], self.board[x][y-1] = self.board[x][y-1], self.board[x][y]
            self.empty_tile = (x, y-1)
        elif direction == 'right' and y < 2:
            self.board[x][y], self.board[x][y+1] = self.board[x][y+1], self.board[x][y]
            self.empty_tile = (x, y+1)

    def can_move(self, direction):
        x, y = self.empty_tile
        return (direction == 'up' and x > 0) or (direction == 'down' and x < 2) or (direction == 'left' and y > 0) or (direction == 'right' and y < 2)

    def is_solved(self):
        return self.board == self.generate_solved_board()

def solve_step(puzzle, n, limit):
    if n > limit:
        puzzle.ATTEMPS += 1
        return -1
    if puzzle.is_solved():
        puzzle.solved_at = n
        puzzle.solution = copy.deepcopy(puzzle.memory.copy())
        return n
    opposite_actions = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
    last_action = puzzle.memory[-1] if puzzle.memory else None

    # try moving up
    if puzzle.can_move('up') and 'up' != opposite_actions.get(last_action):
        puzzle.move_tile('up')
        puzzle.memory.append('up')
        puzzle.print_board()
        sel = solve_step(puzzle, n+1, limit)
        if puzzle.is_solved():
            return sel
        puzzle.move_tile('down')
        puzzle.memory.pop()

    # try moving down
    if puzzle.can_move('down') and 'down' != opposite_actions.get(last_action):
        puzzle.move_tile('down')
        puzzle.memory.append('down')
        puzzle.print_board()
        sel = solve_step(puzzle, n+1, limit)
        if puzzle.is_solved():
            return sel
        puzzle.move_tile('up')
        puzzle.memory.pop()

    # try moving left
    if puzzle.can_move('left') and 'left' != opposite_actions.get(last_action):
        puzzle.move_tile('left')
        puzzle.memory.append('left')
        puzzle.print_board()
        sel = solve_step(puzzle, n+1, limit)
        if puzzle.is_solved():
            return sel
        puzzle.move_tile('right')
        puzzle.memory.pop()

    # try moving right
    if puzzle.can_move('right') and 'right' != opposite_actions.get(last_action):
        puzzle.move_tile('right')
        puzzle.memory.append('right')
        puzzle.print_board()
        sel = solve_step(puzzle, n+1, limit)
        if puzzle.is_solved():
            return sel
        puzzle.move_tile('left')
        puzzle.memory.pop()


def solve_puzzle(puzzle):
    puzzle.print_board()
    steps = solve_step(puzzle, 0, 40)
    puzzle.print_board()
    puzzle.print_original()
    print('Solved in', puzzle.solved_at, 'steps')
    print('Solution:', puzzle.solution)

# Example usage
puzzle = PuzzleBoard()
puzzle.print_board()
solve_puzzle(puzzle)
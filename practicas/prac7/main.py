import random

class TTT:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.moves = 0

    def print_board(self):
        print("Current board:")
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
        print()

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.moves += 1
            if self.check_winner(row, col):
                self.winner = self.current_player
            elif self.moves == 9:
                self.winner = 'Draw'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
        return False

    def position_eval(self, row, col):
        if self.board[row][col] != ' ':
            return 0  # Position is already occupied

        score = 0

        # Check if the position is in the center
        if row == 1 and col == 1:
            score += 3

        # Check adjacent positions for 'O'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] == 'O':
                score += 1

        # Add +2 if not in the center but no 'X' on the opposite side of the center
        if (row, col) != (1, 1):
            opposite_row, opposite_col = 2 - row, 2 - col
            if self.board[opposite_row][opposite_col] != 'X':
                score += 2

        # Add +3 if the move wins the game
        self.board[row][col] = self.current_player  # Simulate the move
        if self.check_winner(row, col):
            score += 3
        self.board[row][col] = ' '  # Revert the move

        return score

    def ai_core(self):
        # Check if AI can win in the next move
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'O'
                    if self.check_winner(row, col):
                        return (row, col)
                    self.board[row][col] = ' '

        # Check if the opponent can win in the next move and block them
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X'
                    if self.check_winner(row, col):
                        self.board[row][col] = 'O'

    def ai_play(self):
        b_score = 0
        b_move = None
        empty_spaces = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
        print(f"Empty spaces: {empty_spaces}")
        for empty in empty_spaces:
            self.board[empty[0]][empty[1]] = 'O'
            if self.ai_play():
                return empty
            # eval = self.position_eval(row, col)
            # if eval > b_score:
            #     b_score = eval
            #     b_move = (row, col)

    def enemy_play(self):
        b_score = 0
        b_move = None
        empty_spaces = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
        print(f"Empty spaces: {empty_spaces}")
        for empty in empty_spaces:
            self.board[empty[0]][empty[1]] = 'X'
            row, col = empty
            eval = self.position_eval(row, col)
            if eval > b_score:
                b_score = eval
                b_move = (row, col)
            self.board[row][col] = ' '
        return b_move

def play_agains_ai():
    game = TTT()
    while game.winner is None:
        game.print_board()
        if game.current_player == 'X':
            row, col = map(int, input("Enter your move (row and column): ").split())
        else:
            # AI move (random for simplicity)
            row, col = game.ai_play()
            print(f"AI chose: {row} {col}")
        game.make_move(row, col)
    game.print_board()
    if game.winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"The winner is: {game.winner}")

play_agains_ai()
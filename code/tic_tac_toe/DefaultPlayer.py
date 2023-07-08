from Player import Player
import random
# set Default as second player

class DefaultPlayer(Player):
    def __init__(self):
        self.breed = 'default'

    def move(self, board):
        default = 'O'
        opponent = 'X'  # The default player as second player

        # Check if there's a winning move for the opponent and block it
        for move in self.available_moves(board):
            new_board = board[:move - 1] + list(opponent) + board[move:]
            if self.has_winner(opponent, new_board):
                return move

        # Check if there's a winning move for the player and make it
        for move in self.available_moves(board):
            new_board = board[:move - 1] + list(default) + board[move:]
            if self.has_winner(default, new_board):
                return move

        # If no winning move for the player or the opponent, choose a random move
        return random.choice(self.available_moves(board))

    def has_winner(self, player, board):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]

        for positions in winning_positions:
            if all(board[pos] == player for pos in positions):
                return True

        return False

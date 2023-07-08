from Player import Player
import random
# set Default as second player

class DefaultPlayer(Player):
    def __init__(self):
        self.breed = 'default'

    def pick_best_move(self, board, piece):
        valid_locations = self.get_valid_locations(board)

        # Check for a winning move
        for col in valid_locations:
            temp_board = board.copy()
            # self.drop_piece(temp_board, col, piece)
            for r in range(board.shape[0]):
                if board[r][col] == 0:
                    row = r
            temp_board[row][col] = piece
            if self.is_winning_move(temp_board, piece):  # need to change
                return col

        # Check for a blocking move
        opponent_piece = 1 if piece == 2 else 2
        for col in valid_locations:
            temp_board = board.copy()
            # self.drop_piece(temp_board, col, opponent_piece)  # need to change
            for r in range(board.shape[0]):
                if board[r][col] == 0:
                    row = r
            temp_board[row][col] = opponent_piece
            if self.is_winning_move(temp_board, opponent_piece):  # need to change
                return col

        # If no winning or blocking move, return a random move
        return random.choice(valid_locations)

    def is_winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(board.shape[1] - 3):
            for r in range(board.shape[0]):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(board.shape[1]):
            for r in range(board.shape[0] - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(board.shape[1] - 3):
            for r in range(board.shape[0] - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(board.shape[1] - 3):
            for r in range(3, board.shape[0]):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True
class Player(object):
    def __init__(self):
        self.breed = 'human'

    def start_game(self):  # QLearning need to override this method
        pass

    def pick_best_move(self, board, piece):
        return int(input("Player 1 Make your Selection (0-6):"))

    def get_valid_locations(self, board):
        valid_locations = []
        column_count = 7  # Get the number of columns from the board's shape
        row_count = 6  # Get the number of rows from the board's shape
        for col in range(column_count):
            # if board.is_valid_location(board, col):
            if board[row_count - 1][col] == 0:
                valid_locations.append(col)
        return valid_locations

    def reward(self, value, board):  # QLearning Player should override this method
        pass
from Player import Player
import random
# set Default as second player
AI_PIECE = 1
PLAYER_PIECE = 2
EMPTY = 0
WINDOW_LENGTH = 4

class MinimaxPlayer(Player):
    def __init__(self):
        self.breed = 'minimax'

    def is_terminal_node(self, board):
        return self.has_winning_move(board, PLAYER_PIECE) or self.has_winning_move(board, AI_PIECE) or len(
            self.get_valid_locations(board)) == 0

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.has_winning_move(board, AI_PIECE):
                    return (None, 100000000000000)
                elif self.has_winning_move(board, PLAYER_PIECE):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, self.score_position(board, AI_PIECE))
        if maximizingPlayer:
            value = float('-inf')
            column = random.choice(valid_locations)
            for col in valid_locations:
                # row = board.get_next_open_row(board, col)
                for r in range(board.shape[0]):
                    if board[r][col] == 0:
                        row = r
                b_copy = board.copy()
                # board.drop_piece(b_copy, row, col, AI_PIECE)
                b_copy[row][col] = AI_PIECE
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = float('inf')
            column = random.choice(valid_locations)
            for col in valid_locations:
                # row = board.get_next_open_row(board, col)
                for r in range(board.shape[0]):
                    if board[r][col] == 0:
                        row = r
                b_copy = board.copy()
                # board.drop_piece(b_copy, row, col, PLAYER_PIECE)
                b_copy[row][col] = PLAYER_PIECE
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def pick_best_move(self, board, piece):
        col, minimax_score = self.minimax(board, 5, float('-inf'), float('inf'), True)
        if board[board.shape[0] - 1][col] == 0:
            return col

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = PLAYER_PIECE
        if piece == PLAYER_PIECE:
            opp_piece = AI_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board, piece):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board[:, board.shape[1] // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(board.shape[0]):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(board.shape[1] - 3):
                window = row_array[c:c + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score Vertical
        # column_count = board.shape[1]  # Get the number of columns from the board's shape
        for c in range(board.shape[1]):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(board.shape[0] - 3):
                window = col_array[r:r + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score posiive sloped diagonal
        for r in range(board.shape[0] - 3):
            for c in range(board.shape[1] - 3):
                window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(board.shape[0] - 3):
            for c in range(board.shape[1] - 3):
                window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def has_winning_move(self, board, piece):
        column_count = 7
        row_count = 6
        # Check horizontal locations for win
        for c in range(column_count - 3):  # self.column_count - 3
            for r in range(row_count):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(column_count):
            for r in range(row_count - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(column_count - 3):
            for r in range(row_count - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(column_count - 3):
            for r in range(3, row_count):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True
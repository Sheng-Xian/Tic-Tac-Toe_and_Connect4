from Player import Player


# By default, MinimaxPlayer is the first player

class MinimaxPlayer(Player):
    def __init__(self, first_player=True):
        self.breed = 'minimax'
        if first_player:
            self.player = 'X'
            self.opponent = 'O'
        else:
            self.player = 'O'
            self.opponent = 'X'

    def move(self, board):
        # if len(self.available_moves(board)) == 9:
        #     return random.choice([1, 3, 7, 9])

        alpha = float('-inf')
        beta = float('inf')
        depth = 0
        best_move = None
        best_value = float('-inf')
        for move in self.available_moves(board):
            board[move - 1] = self.player
            value = self.min_value(board, alpha, beta, depth + 1)
            board[move - 1] = ' '

            if value > best_value:
                best_value = value
                best_move = move

            # alpha = max(alpha, best_value)
        return best_move

    def terminal_test(self, board):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if self.player == board[a] == board[b] == board[c]:
                return True, 1
            elif self.opponent == board[a] == board[b] == board[c]:
                return True, -1

        if not any([space == ' ' for space in board]):
            return True, 0

        return False, 0

    def max_value(self, board, alpha, beta, depth):
        in_terminal_state, utility_value = self.terminal_test(board)
        if in_terminal_state or depth >= 9:
            return utility_value

        value = float('-inf')
        for move in self.available_moves(board):
            board[move - 1] = self.player
            value = max(value, self.min_value(board, alpha, beta, depth + 1))
            board[move - 1] = ' '

            if beta <= value:
                return value
            alpha = max(alpha, value)

        return value

    def min_value(self, board, alpha, beta, depth):
        in_terminal_state, utility_value = self.terminal_test(board)
        if in_terminal_state or depth >= 9:
            return utility_value

        value = float('inf')
        for move in self.available_moves(board):
            board[move - 1] = self.opponent
            value = min(value, self.max_value(board, alpha, beta, depth + 1))
            board[move - 1] = ' '

            if value <= alpha:
                return value
            beta = min(beta, value)

        return value

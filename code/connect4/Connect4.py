import numpy as np

PLAYER_ONE = 0
PLAYER_TWO = 1

EMPTY = 0
PLAYER1_PIECE = 1
PLAYER2_PIECE = 2

class Connect4:
    def __init__(self, player1, player2):
        self.row_count = 6
        self.column_count = 7
        self.window_length = 4
        self.player1, self.player2 = player1, player2
        self.board = self.create_board(self.row_count, self.column_count)

    def create_board(self, r, c):
        board = np.zeros((r, c))
        return board

    def print_board(self, board):
        print(np.flip(board, 0))

    def board_full(self):
        for col in range(self.column_count):
            for row in range(self.row_count):
                if self.board[row - 1][col - 1] == EMPTY:
                    return False
        return True

    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(self.column_count - 3):
            for r in range(self.row_count):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.column_count):
            for r in range(self.row_count - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(self.column_count - 3):
            for r in range(self.row_count - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(self.column_count - 3):
            for r in range(3, self.row_count):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True

    def play_game(self, train=True):
        game_over = False

        # turn = random.randint(PLAYER, AI)
        turn = PLAYER_ONE # let AI play first

        if not train:
            print('\nNew game!')
            print('Play 1 go first and its piece is 1, Player 2 go second and its piece is 2.')

        while not game_over:

            if turn == PLAYER_ONE:
                if self.player1.breed == "human":
                    self.print_board()
                col = self.player1.pick_best_move(self.board, PLAYER1_PIECE)

                # if self.is_valid_location(self.board, col):
                if self.board[self.row_count - 1][col] == 0:
                    # row = self.get_next_open_row(self.board, col)
                    for r in range(self.row_count):
                        if self.board[r][col] == 0:
                            row = r
                            break
                    # self.drop_piece(self.board, row, col, PLAYER1_PIECE)
                    self.board[row][col] = PLAYER1_PIECE

                    if not train:
                        self.print_board(self.board)
                    if self.winning_move(self.board, PLAYER1_PIECE):
                        self.player1.reward(1, self.board)
                        if not train:
                            print("Player 1 wins!!")
                        # game_over = True
                        return 1
                    if self.board_full():
                        self.player1.reward(0.5, self.board)
                        if not train:
                            print("Draw!!")
                        # game_over = True
                        return 0

                    turn += 1
                    turn = turn % 2


            # # Ask for Player 2 Input
            if turn == PLAYER_TWO and not game_over:
                if self.player2.breed == "human":
                    self.print_board()
                col = self.player2.pick_best_move(self.board, PLAYER2_PIECE)

                if self.board[self.row_count - 1][col] == 0:
                    for r in range(self.row_count):
                        if self.board[r][col] == 0:
                            row = r
                            break
                    self.board[row][col] = PLAYER2_PIECE

                    if not train:
                        self.print_board(self.board)
                    if self.winning_move(self.board, PLAYER2_PIECE):
                        self.player2.reward(-1, self.board)
                        if not train:
                            print("Player 2 wins!!")
                        # game_over = True
                        return -1
                    if self.board_full():
                        self.player2.reward(0.5, self.board)
                        if not train:
                            print("Draw!!")
                        # game_over = True
                        return 0

                    turn += 1
                    turn = turn % 2


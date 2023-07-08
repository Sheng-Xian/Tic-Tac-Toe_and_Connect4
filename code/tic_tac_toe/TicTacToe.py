class TicTacToe:
    def __init__(self, playerX, playerO):
        self.board = [' '] * 9
        self.playerX, self.playerO = playerX, playerO
        self.playerX_turn = True

    def display_board(self):
        print('     |     |     ')
        print('  %s  |  %s  |  %s  ' % (self.board[0],\
                                        self.board[1],\
                                        self.board[2]))
        print('_____|_____|_____')
        print('     |     |     ')
        print('  %s  |  %s  |  %s  ' % (self.board[3],\
                                        self.board[4],\
                                        self.board[5]))
        print('_____|_____|_____')
        print('     |     |     ')
        print('  %s  |  %s  |  %s  ' % (self.board[6],\
                                        self.board[7],\
                                        self.board[8]))
        print('     |     |     ')

    def board_full(self):
        return not any([space == ' ' for space in self.board])

    def player_wins(self, char):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if char == self.board[a] == self.board[b] == self.board[c]:
                return True

        return False

    def play_game(self, train=True):
        if not train:
            print('\nNew game!')
            print('Play 1: X, Player 2: O')

        self.playerX.start_game()
        self.playerO.start_game()
        while True:
            if self.playerX_turn:
                player, char, other_player = self.playerX, 'X', self.playerO
            else:
                player, char, other_player = self.playerO, 'O', self.playerX

            if player.breed == "human":
                self.display_board()

            move = player.move(self.board)
            self.board[move - 1] = char

            if self.player_wins(char):
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                if not train:
                    self.display_board()
                    print(char + ' wins!')
                if char == 'X':
                    return 1
                else:
                    return -1

            if self.board_full():
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                if not train:
                    self.display_board()
                    print('Draw!')
                return 0

            other_player.reward(0, self.board)
            self.playerX_turn = not self.playerX_turn
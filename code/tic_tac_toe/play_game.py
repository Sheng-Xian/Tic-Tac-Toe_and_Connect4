from QLearningPlayer import QLearningPlayer
from TicTacToe import TicTacToe
from DefaultPlayer import DefaultPlayer
from MinimaxPlayer import MinimaxPlayer
import argparse
from timeit import timeit


def train_q(q_player, first_player=True):
    p = DefaultPlayer()
    for i in range(0, 100000):  # Train Qlearning player with Default player
        if first_player:
            t = TicTacToe(q_player, p)
            t.play_game()
        else:
            t = TicTacToe(p, q_player)
            t.play_game()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--player1', nargs='?', default="minimax", type=str)
    parser.add_argument('--player2', nargs='?', default="default", type=str)
    parser.add_argument('--num_games', nargs='?', default=100, type=int)
    args = parser.parse_args()
    player1_type = args.player1
    player2_type = args.player2
    num_games = args.num_games

    if player1_type == "minimax":
        player1 = MinimaxPlayer()
    elif player1_type == "qlearning":
        player1 = QLearningPlayer()
        train_time = timeit(stmt='train_q(player1)', number=1, globals=globals())
        print(f"The train time taken is {train_time}")
        player1.epsilon = 0
    elif player1_type == "default":
        player1 = DefaultPlayer()
    print(f"Player 1 is {player1_type} , Player 2 is {player2_type}")

    if player2_type == "default":
        player2 = DefaultPlayer()
    elif player2_type == "qlearning":
        player2 = QLearningPlayer()
        train_time = timeit(stmt='train_q(player2)', number=1, globals=globals())
        print(f"The train time taken is {train_time}")
        player2.epsilon = 0
    elif player2_type == "minimax":
        player2 = MinimaxPlayer(first_player=False)

    def run_games():
        player1_wins = 0
        player2_wins = 0
        draws = 0
        for _ in range(num_games):
            t = TicTacToe(player1, player2)
            result = t.play_game(train=True)
            if result == 1:
                player1_wins += 1
            elif result == -1:
                player2_wins += 1
            else:
                draws += 1
        print(f"Results after {num_games} games:")
        print(f"Player 1 wins: {player1_wins} ({(player1_wins / num_games) * 100:.2f}%)")
        print(f"Player 2 wins: {player2_wins} ({(player2_wins / num_games) * 100:.2f}%)")
        print(f"Draws: {draws} ({(draws / num_games) * 100:.2f}%)")

    time = timeit(stmt='run_games()', number=1, globals=globals())
    print(f"The time taken is {time}")


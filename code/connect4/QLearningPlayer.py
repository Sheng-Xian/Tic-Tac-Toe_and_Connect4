import numpy as np
import random
from Player import Player

ROW_COUNT = 6
COLUMN_COUNT = 7


class QLearningPlayer(Player):
    def __init__(self):
        self.breed = 'qlearner'
        self.q = {}
        self.epsilon = 0.1
        self.alpha = 0.5  # learning rate
        self.gamma = 0.9  # discount factor
        self.last_state = np.zeros((ROW_COUNT, COLUMN_COUNT))
        self.last_move = None

    def start_game(self):
        self.last_state = np.zeros((ROW_COUNT, COLUMN_COUNT))
        self.last_move = None

    def board_to_tuple(self, board):
        return tuple(map(tuple, board))

    def getQ(self, state, action):
        state = self.board_to_tuple(state)
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = 1.0  # Initial all q as 1

        return self.q.get((state, action))

    def pick_best_move(self, board, piece):
        actions = self.get_valid_locations(board)

        if random.random() < self.epsilon:  # To balance exploration and exploitation
            self.last_move = random.choice(actions)
            self.last_state = self.board_to_tuple(board)
            return self.last_move

        qs = [self.getQ(self.last_state, each) for each in actions]
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.last_move = actions[i]
        self.last_state = self.board_to_tuple(board)

        return self.last_move

    def reward(self, value, board):
        if self.last_move:
            self.learn(self.last_state, self.last_move, value, self.board_to_tuple(board))

    def learn(self, state, action, reward, result_state):
        prev = self.getQ(state, action)
        maxqnew = max(
            [self.getQ(result_state, a) for a in self.get_valid_locations(state)]
        )
        self.q[(state, action)] = prev + \
                                  self.alpha * ((reward + self.gamma * maxqnew) - prev)

import random
from Player import Player


class QLearningPlayer(Player):
    def __init__(self):
        self.breed = 'qlearner'
        self.q = {}
        self.epsilon = 0.1
        self.alpha = 0.1  # learning rate
        self.gamma = 0.9  # discount factor
        self.last_state = (' ',) * 9
        self.last_move = None

    def start_game(self):
        self.last_state = (' ',) * 9
        self.last_move = None

    def getQ(self, state, action):
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = 1.0  # Initial all q as 1

        return self.q.get((state, action))

    def move(self, board):
        actions = self.available_moves(board)

        if random.random() < self.epsilon:  # To balance exploration and exploitation
            self.last_move = random.choice(actions)
            self.last_state = tuple(board)
            return self.last_move

        qs = [self.getQ(self.last_state, each) for each in actions]
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.last_move = actions[i]
        self.last_state = tuple(board)

        return self.last_move

    def reward(self, value, board):
        if self.last_move:
            self.learn(self.last_state, self.last_move, value, tuple(board))

    def learn(self, state, action, reward, result_state):
        prev = self.getQ(state, action)
        maxqnew = max(
            [self.getQ(result_state, a) for a in self.available_moves(state)]
        )
        self.q[(state, action)] = prev + \
            self.alpha * ((reward + self.gamma * maxqnew) - prev)



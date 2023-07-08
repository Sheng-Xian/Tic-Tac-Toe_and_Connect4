This project is to implement Minimax and Reinforcement Learning algorithms for playing 2 games, Tic Tac Toe and Connect 4, and compare their performance.

All code is in the folder code, please unzip it and place in a suitable place.

Prerequisite:
pip install numpy

run below command to see different players competes in Tic Tac Toe and Connect 4 games

#Tic Tac Toe

python play_game.py --player1 "minimax" --player2 "default" 

python play_game.py --player1 "qlearning" --player2 "default" --num_games 100

python play_game.py --player1 "minimax" --player2 "qlearning"

python play_game.py --player1 "qlearning" --player2 "minimax"

#Connect 4

python play_game.py --player1 "minimax" --player2 "default" 

python play_game.py --player1 "qlearning" --player2 "default" 

python play_game.py --player1 "minimax" --player2 "qlearning"

python play_game.py --player1 "qlearning" --player2 "minimax"

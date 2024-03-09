# food_generator.py

import random

def generate_new_food_position(game_board):
    empty_cells = [(i, j) for i in range(len(game_board)) for j in range(len(game_board[0])) if game_board[i][j] == 0]
    return random.choice(empty_cells)
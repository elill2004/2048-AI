from logic import up, down, left, right, game_state, new_game, add_two, reverse, cover_up, transpose, merge, random_move

import numpy as np
import matplotlib as mpl

SEARCH_PARAMS = 200
NUMBER_MOVES = 4
SAMPLE_SIZE = 50

SPM = 10
SL_SCALE = 4

def get_search_params(move_number):
    searches_per_move = SPM * (1+(move_number // SEARCH_PARAMS))
    search_length = SL_SCALE * (1+(move_number // SEARCH_PARAMS))
    return searches_per_move, search_length


def ai_move(searches_per_move, search_length, game):
    first_moves = [up, down, left, right]
    first_move_grades = np.zeros(NUMBER_MOVES)
    for first_move_index in range(NUMBER_MOVES):
        first_move_function = first_moves[first_move_index]
        board_with_first_move, first_move_made, first_move_score = first_move_function(game)
        if first_move_made:
            board_with_first_move = add_two(board_with_first_move)
            first_move_grades[first_move_index] += first_move_score
        else:
            continue
        for _ in range(searches_per_move):
            move_number = 1
            search_board = np.copy(board_with_first_move)
            game_valid = True
            while game_valid and move_number < search_length:
                search_board, game_valid, score = random_move(search_board)
                if game_valid:
                    search_board = add_two(search_board)
                    first_move_grades[first_move_index] += score
                    move_number += 1

    best_move_index = np.argmax(first_move_grades)
    best_move = first_moves[best_move_index]
    search_board, game_valid, score = best_move(game)
    return search_board, game_valid

                





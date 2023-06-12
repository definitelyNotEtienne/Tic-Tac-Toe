"""This code is referred and learned from Ivan. His profiling was used as a reference."""

import timeit
import Tic_Tac_Toe_AI


def generate_board(n):
    ai = Tic_Tac_Toe_AI.AI()
    board = Tic_Tac_Toe_AI.Model()
    for i in range(n):
        row, col = ai.rnd(board)
        board.spots(row, col, ai.player)
        ai.player = ai.player ^ 3
    return board


if __name__ == '__main__':
    n = 9
    repeat = 100
    random_list = []
    minimax_list = []
    for i in range(n):
        ai = Tic_Tac_Toe_AI.AI()
        total_time = 0
        total_time1 = 0
        for j in range(repeat):
            board = generate_board(i)
            total_time += timeit.timeit(stmt="ai.rnd(model)", number=10000, globals=globals()) / 10000
            total_time1 += timeit.timeit(stmt="ai.minimax(model, -100)", number=100, globals=globals()) / 100
        random_list.append(round(total_time / repeat * 1000, 6))
        minimax_list.append(round(total_time1 / repeat * 1000, 6))
    print(random_list)
    print(minimax_list)

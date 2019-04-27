from connectfour.agents.computer_player import RandomAgent
import random
import numpy as np

from connectfour.connect4.mcts_ia import *


class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """
        temp = np.array(board.board);
        mcts = Node(temp, 0, None, None)
        training_time = 20000

        node = train_mcts_once(mcts)


        node = train_mcts_during(node, training_time)
        print([(n.win, n.games) for n in node.children])
        node, move = node.select_move()
        utils_print(node.state)
        row = board.try_move(move)
        return row, move


def utils_print(grid):
    print_grid = grid.astype(str)
    print_grid[print_grid == '-1'] = 'X'
    print_grid[print_grid == '1'] = 'O'
    print_grid[print_grid == '0'] = ' '
    res = str(print_grid).replace("'", "")
    res = res.replace('[[', '[')
    res = res.replace(']]', ']')
    print(' ' + res)
    print('  ' + ' '.join('0123456'))

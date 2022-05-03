from sudoku import Sudoku
import random as r
import copy


class GameGenerator(Sudoku):

    def __init__(self, num_empty):
        super().__init__()
        self.num_empty = num_empty
        self.solve()

    def game_generate(self):
        rounds = 5
        while rounds > 0 and self.num_empty_cells() < 64 and self.num_empty_cells() < self.num_empty:
            row = r.randint(0, 8)
            col = r.randint(0, 8)
            while self.board[row][col] == 0:
                row = r.randint(0, 8)
                col = r.randint(0, 8)
            removed_val = self.board[row][col]
            self.board[row][col] = 0
            if self.num_solutions(row, col) != 1:
                self.board[row][col] = removed_val
                rounds -= 1

    def num_solutions(self, row, col):
        if self.num_empty_cells() == 1:
            return 1
        sol_count = 0
        for i in range(1, 10):
            board_copy = copy.deepcopy(self)
            if board_copy.check_if_valid(row, col, i):
                board_copy.board[row][col] = i
                if board_copy.solve():
                    sol_count += 1
        return sol_count

import random as r
import numpy as np


class Sudoku:

    def __init__(self):
        self.board = np.zeros((9, 9))

    def __str__(self):
        s = ""
        for i in range(9):
            for j in range(9):
                t = int(self.board[i][j])
                if t == 0:
                    t = "*"
                s = s + f"{t} "
                if j % 3 == 2 and j != 8:
                    s = s + "| "
            if i != 8:
                s = s + "\n"
            if i % 3 == 2 and i != 8:
                s = s + "------+-------+------\n"
        return s

    def user_input_board(self):
        print("Enter the numbers in each row separated by spaces. Use 0 for empty cells.")
        for i in range(9):
            row = input(f"Row {i + 1}: ")
            row = row.strip().split(" ")
            row = [int(n) for n in row]
            self.board[i] = row

    def solve(self):
        if self.num_empty_cells() > 64:
            empty_cell = self.find_empty_rand()
        else:
            empty_cell = self.find_empty()
        if not empty_cell:
            return True
        row, col = empty_cell
        for i in range(1, 10):
            if self.check_if_valid(row, col, i):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def find_empty_rand(self):
        row = r.randint(0, 8)
        col = r.randint(0, 8)
        while self.board[row][col] != 0:
            row = r.randint(0, 8)
            col = r.randint(0, 8)
        return row, col

    def num_empty_cells(self):
        n = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    n += 1
        return n

    def not_in_row(self, row, n):
        current_row = self.board[row]
        if n in current_row:
            return False
        return True

    def not_in_col(self, col, n):
        current_col = [row[col] for row in self.board]
        if n in current_col:
            return False
        return True

    def not_in_box(self, row, col, n):
        box_start_row = row - (row % 3)
        box_start_col = col - (col % 3)
        box = self.board[box_start_row:box_start_row+3, box_start_col:box_start_col+3]
        if n in box:
            return False
        return True

    def check_if_valid(self, row, col, n):
        return self.not_in_row(row, n) and self.not_in_col(col, n) and self.not_in_box(row, col, n)

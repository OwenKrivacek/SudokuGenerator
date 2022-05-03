from sudoku import Sudoku
from game_generator import GameGenerator


print("Welcome to my Sudoku generator and solver!")
s_bar = "----------------------------------\n"
s_opt1 = "[1] Get a puzzle to solve\n"
s_opt2 = "[2] Enter a puzzle to be solved\n"
s_opt3 = "[3] Exit\n"
s_act = "Enter the number of the action you would like to perform: "
while True:
    action = input(s_bar + s_opt1 + s_opt2 + s_opt3 + s_act)
    if action == "1":
        num_empty = int(input("How many empty cells should the puzzle have? "))
        puzzle = GameGenerator(num_empty)
        puzzle.game_generate()
        print(puzzle)
    elif action == "2":
        puzzle = Sudoku()
        puzzle.user_input_board()
        puzzle.solve()
        print(puzzle)
    elif action == "3":
        break

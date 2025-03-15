import random
from random import shuffle

class sudoku_board:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = None
        self.generate_solution()
        self.set_difficulty("easy")

    def generate_solution(self):
        for i in [0, 3, 6]:
            self.fill_3x3_box(i, i)
        self.fill_remaining_cells(0, 3)
        self.solution = [row[:] for row in self.board]

    def set_difficulty(self, difficulty):
        self.board = [row[:] for row in self.solution]
        cells_to_remove = {
            "easy": 30,
            "medium": 45,
            "hard": 55
        }
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)
        for i, j in positions[:cells_to_remove[difficulty]]:
            self.board[i][j] = 0

    def fill_3x3_box(self, row_start, col_start):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        index = 0
        for row in [row_start, row_start + 1, row_start + 2]:
            for col in [col_start, col_start + 1, col_start + 2]:
                self.board[row][col] = numbers[index]
                index += 1

    def fill_remaining_cells(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return self.fill_remaining_cells(row + 1, 0)
        if self.board[row][col] != 0:
            return self.fill_remaining_cells(row, col + 1)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(numbers)

        for num in numbers:
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining_cells(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True

    def check_solution(self, row, col, num):
        return self.solution[row][col] == num

    def get_solution(self, row, col):
        return self.solution[row][col]

    def place_number(self, row, col, num):
        if self.check_solution(row, col, num):
            self.board[row][col] = num
            return True
        return False

    def is_completed(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.solution[i][j]:
                    return False
        return True

    def get_board(self):
        return self.board

    def is_cell_empty(self, row, col):
        return self.board[row][col] == 0
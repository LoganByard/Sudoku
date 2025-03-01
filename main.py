import random
from operator import truth
from random import shuffle


class sudoku_board:
    def __init__(self):
        rows, cols = (9, 9)
        self.board = [[0 for i in range(cols)] for j in range(rows)]
        for i in [0, 3, 6]:
            self.fill_3x3_box(i, i)
        self.fill_remaining_cells(0, 3)


    def fill_3x3_box(self, row_start, col_start):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        index = 0
        for row in [row_start, row_start+1, row_start+2]:
            for col in [col_start, col_start+1, col_start+2]:
                self.board[row][col] = numbers[index]
                index += 1

    def fill_remaining_cells(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return self.fill_remaining_cells(row + 1, 0)
        if self.board[row][col] != 0:
            return self.fill_remaining_cells(row, col+1)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(numbers)

        for num in numbers:
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining_cells(row, col+1):
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



board = sudoku_board()
for i in range(9):
    print (board.board[i])



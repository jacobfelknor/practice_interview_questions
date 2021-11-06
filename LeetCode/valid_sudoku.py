"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # rows
    for row in board:
        entries = set()
        for elem in row:
            if elem == ".":
                continue
            if elem in entries:
                return False
            entries.add(elem)

    # columns
    for ii in range(9):
        col = [x[ii] for x in board]
        entries = set()
        for elem in col:
            if elem == ".":
                continue
            if elem in entries:
                return False
            entries.add(elem)

    # boxes
    for start in [0, 3, 6]:
        for ii in [0, 3, 6]:
            entries = set()
            for jj in range(start, 3 + start):
                for entry in board[jj][ii : ii + 3]:
                    if entry == ".":
                        continue
                    if entry in entries:
                        return False
                    entries.add(entry)

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", "4", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


print(isValidSudoku(board))

import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # * check values in row and column
        for x in range(9):
            # check values in row
            row_unique = set()
            for i in range(9):
                if board[x][i] == ".":
                    continue
                if board[x][i] in row_unique:
                    return False
                row_unique.add(board[x][i])

            # check values in column
            column_unique = set()
            for i in range(9):
                if board[i][x] == ".":
                    continue
                if board[i][x] in column_unique:
                    return False
                column_unique.add(board[i][x])

        # * check unique values in 3x3 square
        for loop in range(9):
            square_x_offset = loop // 3
            square_y_offset = loop % 3
            square_unique = set()
            for x_offset in range(3):
                for y_offset in range(3):
                    logger.debug(
                        f"{loop=}, {square_x_offset=}, {square_y_offset=}"
                        f" => ({square_x_offset * 3 + x_offset},{square_y_offset * 3 + y_offset})"
                    )

                    target_x = square_x_offset * 3 + x_offset
                    target_y = square_y_offset * 3 + y_offset

                    if board[target_x][target_y] == ".":
                        continue

                    if board[target_x][target_y] in square_unique:
                        square_start = (square_x_offset * 3, square_y_offset * 3)
                        square_finish = (square_x_offset * 3 + 3, square_y_offset * 3 + 3)
                        logger.error(f"duplicated value in {square_start} ~ {square_finish}")
                        return False

                    square_unique.add(board[target_x][target_y])

        return True


@pytest.mark.parametrize(
    "board, expected",
    (
        [
            [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ],
        [
            [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ],
    ),
)
def test_valid_sudoku(board: List[List[str]], expected: bool):
    solution = Solution()
    assert solution.isValidSudoku(board) == expected

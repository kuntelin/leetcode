import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        logger.debug(f"{row=},{col=}")

        def binary_search(left_boundary: int, right_boundary: int) -> bool:
            logger.info(f"binary_search({left_boundary=}, {right_boundary=})")

            if left_boundary > right_boundary:
                logger.info("boundary cross over, target not found!")
                return False

            middle_idx = (left_boundary + right_boundary) // 2

            middle_row = middle_idx // col
            middle_col = middle_idx % col

            logger.debug(f"{middle_idx=},{middle_row=},{middle_col=}")
            logger.debug(f"{target=},{matrix[middle_row][middle_col]=}")

            if matrix[middle_row][middle_col] == target:
                logger.info("target found!")
                return True
            elif matrix[middle_row][middle_col] > target:
                logger.debug("target in lower boundary")
                return binary_search(left_boundary, middle_idx - 1)
            elif matrix[middle_row][middle_col] < target:
                logger.debug("target in upper boundary")
                return binary_search(middle_idx + 1, right_boundary)
            else:
                raise Exception("this line should not be reached!")

            return False

        return binary_search(0, row * col - 1)


param_names = "matrix,target,expected"
param_values = [
    ([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([[1], [3]], 1, True),
    ([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10, True),
]


@pytest.mark.parametrize(param_names, param_values)
def test_search_a_2d_matrix(benchmark, matrix: List[List[int]], target: int, expected: bool):
    solution = Solution()
    result = benchmark(solution.searchMatrix, matrix, target)
    assert result == expected

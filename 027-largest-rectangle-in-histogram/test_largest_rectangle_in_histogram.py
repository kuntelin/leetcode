import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """ """
        logger.debug(f"{heights=}")

        largest = 0
        stack = []  # pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                largest = max(largest, height * (i - idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))

        return largest


param_names = "heights,expected"
param_values = [
    ([7, 1, 7, 2, 2, 4], 8),
    ([1, 3, 7], 7),
    ([2, 1, 5, 6, 2, 3, 0], 10),
]


@pytest.mark.parametrize(param_names, param_values)
def test_largest_rectangle_in_histogram(benchmark, heights: List[int], expected: int):
    solution = Solution()
    result = benchmark(solution.largestRectangleArea, heights)
    assert result == expected

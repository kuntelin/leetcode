import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        raise NotImplementedError


param_names = "heights,expected"
param_values = [
    ([7, 1, 7, 2, 2, 4], 8),
    ([1, 3, 7], 7),
]


@pytest.mark.parametrize(param_names, param_values)
def test_largest_rectangle_in_histogram(benchmark, heights: List[int], expected: int):
    solution = Solution()
    result = benchmark(solution.largestRectangleArea, heights)
    assert result == expected

import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_idx, r_idx = 0, len(heights) - 1
        answer = -1
        while l_idx < r_idx:
            # calculate the amount of index l_idx and r_idx
            amount = min(heights[l_idx], heights[r_idx]) * (r_idx - l_idx)
            logger.debug(f"amount of {heights[l_idx]=} and {heights[r_idx]=} is {amount=}")

            # get the maximum value
            answer = max(answer, amount)
            logger.debug(f"current maximum value is {answer}")

            if heights[l_idx] < heights[r_idx]:
                l_idx += 1
                continue

            if heights[l_idx] > heights[r_idx]:
                r_idx -= 1
                continue

            # both the height of l_idx and r_idx are the same, move left index
            l_idx += 1

        return answer


param_names = "heights, expected"
param_values = (
    ([1, 7, 2, 5, 4, 7, 3, 6], 36),
    ([2, 2, 2], 4),
)


@pytest.mark.parametrize(param_names, param_values)
def test_container_with_most_water(benchmark, heights: List[int], expected: int):
    solution = Solution()

    result = benchmark(solution.maxArea, heights)
    assert result == expected
    # assert False

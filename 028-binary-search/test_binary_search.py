import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(left_idx: int, right_idx: int) -> int:
            logger.debug(f"search target in {left_idx} to {right_idx}")

            if left_idx > right_idx:
                logger.debug("cross the lower and upper boundary, return -1")
                return -1

            middle_idx = (left_idx + right_idx + 1) // 2

            logger.debug(f"{middle_idx=}, {nums[middle_idx]=}")
            if nums[middle_idx] > target:
                logger.debug("target in lower bound")
                return bin_search(left_idx, middle_idx - 1)
            elif nums[middle_idx] < target:
                logger.debug("target in upper bound")
                return bin_search(middle_idx + 1, right_idx)
            else:
                logger.debug(f"find target at index {middle_idx}")
                return middle_idx

        return bin_search(0, len(nums) - 1)


param_names = "nums,target,expected"
param_values = [
    ([-1, 0, 2, 4, 6, 8], 4, 3),
    ([-1, 0, 2, 4, 6, 8], 3, -1),
    ([-1, 0, 3, 5, 9, 12], 13, -1),
]


@pytest.mark.parametrize(param_names, param_values)
def test_binary_search(benchmark, nums: List[int], target: int, expected: int):
    solution = Solution()
    result = benchmark(solution.search, nums, target)
    assert result == expected

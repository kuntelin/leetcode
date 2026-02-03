import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, l_idx, r_idx = [], 0, 0
        for r_idx in range(len(nums)):
            if r_idx - l_idx + 1 < k:
                continue

            if r_idx - l_idx + 1 == k:
                logger.info("match the window size, get the max number in the window")
                logger.debug(f"{l_idx=}, {r_idx=}, {nums[l_idx:r_idx+1]=}, {max(nums[l_idx:r_idx+1])=}")
                res.append(max(nums[l_idx : r_idx + 1]))
                l_idx += 1
                continue

            logger.debug("You should not see this message.")

        return res


param_names = "nums,k,expected"
param_values = [
    ([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6]),
]


@pytest.mark.parametrize(param_names, param_values)
def test_permutation_in_string(benchmark, nums: List[int], k: int, expected: List[int]):
    solution = Solution()

    result = benchmark(solution.maxSlidingWindow, nums, k)
    assert result == expected

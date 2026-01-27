import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        possible_hash = {}
        for i, target in enumerate(nums):
            logger.debug(f"{i=}, {target=}")

            # target greater than zero, there is no possible value
            if target > 0:
                break

            # find the possible combinations
            l_idx = i + 1
            r_idx = len(nums) - 1
            while l_idx < r_idx and l_idx != r_idx:
                if nums[l_idx] + nums[r_idx] + target < 0:
                    l_idx += 1
                    continue

                if nums[l_idx] + nums[r_idx] + target > 0:
                    r_idx -= 1
                    continue

                if nums[l_idx] + nums[r_idx] + target == 0:
                    possible_hash[",".join([str(x) for x in [target, nums[l_idx], nums[r_idx]]])] = [
                        target,
                        nums[l_idx],
                        nums[r_idx],
                    ]

                l_idx += 1
                r_idx -= 1

        logger.debug(f"{possible_hash.values()=}")

        return list(possible_hash.values())


param_names = "nums, expected"
param_values = (
    (
        [-1, 0, 1, 2, -1, -4],
        [[-1, -1, 2], [-1, 0, 1]],
    ),
    (
        [0, 0, 0],
        [[0, 0, 0]],
    ),
    (
        [0, 0, 0, 0],
        [[0, 0, 0]],
    ),
    (
        [-2, 0, 1, 1, 2],
        [[-2, 0, 2], [-2, 1, 1]],
    ),
)


@pytest.mark.parametrize(param_names, param_values)
def test_3_sum(benchmark, nums: List[int], expected: List[int]):
    solution = Solution()

    result = benchmark(solution.threeSum, nums)
    assert result == expected

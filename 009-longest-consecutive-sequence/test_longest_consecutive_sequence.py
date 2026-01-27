import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        logger.debug(f"{sorted_nums=}")

        prev_number = None
        current_longest = 0
        final_longest = 0
        for idx, current_number in enumerate(sorted_nums):
            if idx == 0:
                # first time into loop
                current_longest += 1
                prev_number = current_number
            elif current_number == prev_number:
                # same number, keep going
                continue
            elif current_number == (prev_number + 1):
                # next number, extends the longest
                current_longest += 1
                prev_number = current_number
            else:
                # not next number, reset and get the longest
                final_longest = max(current_longest, final_longest)

                current_longest = 1
                prev_number = current_number

        return max(current_longest, final_longest)


param_names = "nums, expected"
param_values = (
    ([2, 20, 4, 10, 3, 4, 5], 4),
    ([0, 3, 2, 5, 4, 6, 1, 1], 7),
)


@pytest.mark.parametrize(param_names, param_values)
def test_longest_consecutive_sequence(benchmark, nums: List[int], expected: int):
    solution = Solution()

    result = benchmark(solution.longestConsecutive, nums)
    assert result == expected

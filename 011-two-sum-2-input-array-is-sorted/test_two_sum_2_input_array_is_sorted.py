import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_idx, r_idx = 0, len(numbers) - 1
        while l_idx < r_idx:
            if numbers[l_idx] + numbers[r_idx] == target:
                logger.debug("target is satisfy!")
                break

            if numbers[l_idx] + numbers[r_idx] > target:
                r_idx -= 1
                continue

            if numbers[l_idx] + numbers[r_idx] < target:
                l_idx += 1
                continue

            logger.debug("why you run here?  O.o?")

        if l_idx >= r_idx:
            raise ValueError("can not find two sum equals target...")

        logger.debug(f"target {target} is satisfy by {l_idx=}:{numbers[l_idx]}, {r_idx=}:{numbers[r_idx]}")

        return [l_idx + 1, r_idx + 1]


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([1, 2, 3, 4], 3, [1, 2]),
        ([2, 3, 4], 6, [0, 2]),
    ],
)
def test_two_sum_2_input_array_is_sorted(numbers: List[int], target: int, expected: List[int]):
    solution = Solution()
    solution.twoSum(numbers, target)
    assert True

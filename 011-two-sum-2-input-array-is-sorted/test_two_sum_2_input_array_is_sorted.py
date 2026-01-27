import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        logger.debug(f"find {target=} in {numbers=}")

        l_idx, r_idx = 0, len(numbers) - 1
        while l_idx < r_idx:
            logger.debug(f"check {l_idx=}::{numbers[l_idx]=}, {r_idx=}::{numbers[r_idx]=}")

            if (numbers[l_idx] + numbers[r_idx]) == target:
                logger.info(f"{target=} satisfied by {numbers[l_idx]=} and {numbers[r_idx]=}")
                break

            if (numbers[l_idx] + numbers[r_idx]) > target:
                r_idx -= 1
                continue

            if (numbers[l_idx] + numbers[r_idx]) < target:
                l_idx += 1
                continue

            logger.debug("why you run here?  O.o?")

        if l_idx >= r_idx:
            logger.info("can not find answer...")
            raise ValueError("can not find two sum equals target...")

        # returned value should be 1 indexed
        return [l_idx + 1, r_idx + 1]


param_names = "numbers, target, expected"
param_values = (
    ([1, 2, 3, 4], 3, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
)


@pytest.mark.parametrize(param_names, param_values)
def test_two_sum_2_input_array_is_sorted(benchmark, numbers: List[int], target: int, expected: List[int]):
    solution = Solution()

    result = benchmark(solution.twoSum, numbers, target)
    assert result == expected

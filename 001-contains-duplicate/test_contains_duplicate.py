from typing import List

import pytest


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        for v in nums:
            if v in exists:
                return True
            exists[v] = True

        return False


param_names = "nums, expected"
param_values = (
    ([1, 2, 3, 3], True),
    ([1, 2, 3, 4], False),
)


@pytest.mark.parametrize(param_names, param_values)
def test_contains_duplicate(benchmark, nums: List[int], expected: bool):
    solution = Solution()

    result = benchmark(solution.hasDuplicate, nums)
    assert result == expected

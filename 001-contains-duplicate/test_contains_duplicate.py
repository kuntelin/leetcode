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


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 3], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_solution01(nums: List[int], expected: bool):
    solution = Solution()
    assert solution.hasDuplicate(nums) == expected

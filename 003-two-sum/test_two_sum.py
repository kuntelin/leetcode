import pytest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for f_idx in range(len(nums)):
            for s_idx in range(f_idx+1, len(nums)):
                if nums[f_idx] + nums[s_idx] == target:
                    return [f_idx, s_idx]



@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([3, 4, 5, 6], 7, [0, 1]),
        ([4, 5, 6], 10, [0, 2]),
        ([5, 5], 10, [0, 1]),
    ],
)
def test_two_sum(nums: List[int], target: int, expected: bool):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected

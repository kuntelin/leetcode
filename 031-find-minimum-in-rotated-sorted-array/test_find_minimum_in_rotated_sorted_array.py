import logging
import math
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """由左右逼近，每次位移一位，執行次數與數量一致"""
        left, right = 0, len(nums) - 1
        ans = math.inf
        cnt = 0
        while left <= right:
            cnt += 1
            if nums[left] <= nums[right]:
                ans = min(ans, nums[left])
                right = left - 1
            else:
                left = left + 1
        logger.debug(f"loop for {cnt} time(s)")

        return ans

    def findMin2(self, nums: List[int]) -> int:
        """左右逼近，每次位移一半的距離，數量越多節省的次數越多"""
        left, right = 0, len(nums) - 1
        cnt = 0
        while left < right:
            cnt += 1
            middle = left + (right - left) // 2  # 位移一半的距離

            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        logger.debug(f"loop for {cnt} time(s)")

        return nums[left]


param_names = "nums,expected"
param_values = [
    ([3, 4, 5, 6, 1, 2], 1),
    ([4, 5, 0, 1, 2, 3], 0),
    ([4, 5, 6, 7], 4),
]


@pytest.mark.parametrize(param_names, param_values)
def test_find_minimum_in_rotated_sorted_array(benchmark, nums: List[int], expected: int):
    solution = Solution()
    result = benchmark(solution.findMin, nums)
    assert result == expected


@pytest.mark.parametrize(param_names, param_values)
def test_find_minimum_in_rotated_sorted_array2(benchmark, nums: List[int], expected: int):
    solution = Solution()
    result = benchmark(solution.findMin2, nums)
    assert result == expected

import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """找出數值由大變小的位置，將其拆分二區塊做查找"""

        def index_of_pivot(numbers: List[int]) -> int:
            """找出數值由大變小的位置"""
            left, right = 0, len(numbers) - 1
            while left < right:
                middle = (left + right) // 2
                if numbers[middle] > numbers[right]:
                    left = middle + 1
                else:
                    right = middle

            return left

        def binary_search(left: int, right: int, target_value: int) -> int:
            """用二分搜尋法找目標值，沒找到回傳-1"""
            while left <= right:
                middle = (left + right) // 2

                logger.debug(f"{left=}, {right=}, {middle=}, {target=}, {nums[left]=}, {nums[right]=}, {nums[middle]=}")

                if nums[middle] > target_value:
                    right = middle - 1
                elif nums[middle] < target_value:
                    left = middle + 1
                else:
                    return middle

            return -1

        pivot = index_of_pivot(numbers=nums)
        logger.debug(f"{pivot=}, {nums[pivot]=}, {nums=}")

        # 查找PIVOT的左半部
        result = binary_search(left=0, right=pivot - 1, target_value=target)
        if result != -1:
            return result

        # 左半部沒找到，查找PIVOT的右半部
        return binary_search(left=pivot, right=len(nums) - 1, target_value=target)


param_names = "nums,target,expected"
param_values = [
    ([3, 4, 5, 6, 1, 2], 1, 4),
    ([3, 5, 6, 0, 1, 2], 4, -1),
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([1], 1, 0),
    ([1, 3], 3, 1),
]


@pytest.mark.parametrize(param_names, param_values)
def test_search_in_rotated_sorted_array(benchmark, nums: List[int], target: int, expected: int):
    solution = Solution()
    result = benchmark(solution.search, nums, target)
    assert result == expected

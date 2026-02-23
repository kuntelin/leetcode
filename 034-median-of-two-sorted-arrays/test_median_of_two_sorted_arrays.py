import logging
from math import inf
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        中位數剛好會在合併後的陣列中央，並且中位數的左半部會小於右半部，
        因此二個陣列也可以分別拆成二半(中位數以左及中位數以右)，
            a_numbers =>    | ... a_left (中位數) a_right ... |
            b_numbers =>    | ... b_left (中位數) b_right ... |
        除此之外，a_left一定會小於或等於b_right及b_left一定會小於或等於a_right，
        由此特性，我們可以定位出中位數在二個陣列的位置，
        如果總數量為奇數時，需回傳二個中間數的最小值，
        如果總數量為偶數時，需回傳左半邊的最大值及右半邊的最小值的平均數
        """

        a_nums, b_nums = nums1, nums2

        # 交換陣列，讓b_nums大於a_nums，方便做計算
        if len(b_nums) < len(a_nums):
            a_nums, b_nums = b_nums, a_nums
        logger.debug(f"{a_nums=}, {b_nums=}")

        # 所有數字的個數及中間的位置
        total = len(a_nums) + len(b_nums)
        half = total // 2
        median_left, median_right = 0, len(a_nums) - 1

        counter = 1000  # 避免無窮迴圈
        while counter and True:
            counter -= 1

            # 找出可能的中間位置
            a_middle = (median_left + median_right) // 2  # 使用a_nums做中間位數的定位
            b_middle = half - a_middle - 2  # 陣列皆以0開始，且有二個，故減去2
            logger.debug(f"{a_middle=}, {b_middle=}")

            a_left = a_nums[a_middle] if a_middle >= 0 else -inf
            a_right = a_nums[a_middle + 1] if (a_middle + 1) < len(a_nums) else inf
            b_left = b_nums[b_middle] if b_middle >= 0 else -inf
            b_right = b_nums[b_middle + 1] if (b_middle + 1) < len(b_nums) else inf
            logger.debug(f"{a_left=}, {a_right=}, {b_left=}, {b_right=}")

            if a_left <= b_right and b_left <= a_right:
                logger.debug("condition 1")
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return float(max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                logger.debug("condition 2")
                median_right = a_middle - 1
            else:
                logger.debug("condition 3")
                median_left = a_middle + 1


param_names = "nums1,nums2,expected"
param_values = [
    ([1, 2], [3], 2.0),
    ([1, 3], [2, 4], 2.5),
    ([], [1], 1.0),
]


@pytest.mark.parametrize(param_names, param_values)
def test_search_in_rotated_sorted_array(benchmark, nums1: List[int], nums2: List[int], expected: float):
    solution = Solution()
    result = benchmark(solution.findMedianSortedArrays, nums1, nums2)
    assert result == expected

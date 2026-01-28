import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        資料結構可視為一個「容器」，因此只需要從外圍往中心進行計算。
        對於每個位置，能接到的雨水量取決於該位置高度，與左右兩側較小的最大高度之間的差值。
        採用「外側包住內側」的雙指標方式計算：
        - 從左右兩端向內移動
        - 持續記錄目前遇到的最大高度
        - 指標先移動，再計算高度差，才能正確判斷該位置能累積的水量
        """

        logger.debug(f"{heights=}")

        l_idx, r_idx = 0, len(heights) - 1
        l_max, r_max = heights[l_idx], heights[r_idx]
        res = 0
        while l_idx < r_idx:
            if l_max < r_max:
                l_idx += 1
                l_max = max(l_max, heights[l_idx])
                res += l_max - heights[l_idx]
            else:
                r_idx -= 1
                r_max = max(r_max, heights[r_idx])
                res += r_max - heights[r_idx]

        return res


param_names = "height,expected"
param_values = [
    ([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
]


@pytest.mark.parametrize(param_names, param_values)
def test_container_with_most_water(benchmark, height, expected):
    solution = Solution()

    result = benchmark(solution.trap, height)
    assert result == expected

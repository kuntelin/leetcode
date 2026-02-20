import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """運用二分法，找出剛好可以符合在h內的最小速率"""

        left = 1
        right = max(piles)
        ans = right  # 先把速率設定為最大值，再往下找符合時間內的最小值
        while left <= right:
            speed = (left + right) // 2
            total_time = 0
            for p in piles:
                total_time += (p + speed - 1) // speed  # 速率的最小正整數, EX: p=3, speed=2, 則需要2h吃完
            logger.debug(f"{speed=},{total_time=}")

            if total_time <= h:
                ans = speed
                right = speed - 1
            else:
                left = speed + 1

        return ans


param_names = "piles,h,expected"
param_values = [
    ([1, 4, 3, 2], 9, 2),
    ([25, 10, 23, 4], 4, 25),
]


@pytest.mark.parametrize(param_names, param_values)
def test_koko_eating_bananas(benchmark, piles: List[int], h: int, expected: int):
    solution = Solution()
    result = benchmark(solution.minEatingSpeed, piles, h)
    assert result == expected

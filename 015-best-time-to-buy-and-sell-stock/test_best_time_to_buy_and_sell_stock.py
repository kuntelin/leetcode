import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        logger.debug(f"{prices=}")

        max_profit = 0
        for buy_idx in range(len(prices)):
            for sell_idx in range(buy_idx + 1, len(prices)):
                max_profit = max(max_profit, prices[sell_idx] - prices[buy_idx])

        return max_profit if max_profit > 0 else 0


param_names = "prices,expected"
param_values = [
    ([10, 1, 5, 6, 7, 1], 6),
    ([[10, 8, 7, 5, 2], 0]),
]


@pytest.mark.parametrize(param_names, param_values)
def test_best_time_to_buy_and_sell_stock(benchmark, prices: List[int], expected: int):
    solution = Solution()

    result = benchmark(solution.maxProfit, prices)
    assert result == expected

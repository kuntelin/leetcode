import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        for idx1 in range(len(temperatures)):
            for idx2 in range(idx1 + 1, len(temperatures)):
                if (temperatures[idx2] - temperatures[idx1]) > 0:
                    ans[idx1] = idx2 - idx1
                    break

        return ans

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        """
        用ans記錄最後的結果並預設都未找到更高的溫度，
        用not_found_stack記錄目前尚未找到更高溫度的索引及溫度，
        依序執行temperatures的項目
        當not_found_stack不為空且目前溫度高於not_found_stack最後一個數值時，
        更新並移除not_found_stack的最後一個數值，
        再次檢查not_found_stack直到不符合判斷，
        將目前的索引及溫度加入not_found_stack中，
        **因為"current_temperature > not_found_stack[-1][1]"的判斷，
        會造成not_found_stack內的數值會一直呈現水平或下滑，
        所以不需要把not_found_stack從頭到尾檢查過**
        """
        ans = [0] * len(temperatures)
        not_found_stack = []  # records the items that has not found the greater temperature
        for current_idx, current_temperature in enumerate(temperatures):
            # check all items in not found stack
            while not_found_stack and current_temperature > not_found_stack[-1][1]:
                not_found_idx, _ = not_found_stack.pop()
                ans[not_found_idx] = current_idx - not_found_idx

            # append current item to not found stack
            not_found_stack.append((current_idx, current_temperature))

        return ans


param_names = "temperatures,expected"
param_values = [
    ([30, 38, 30, 36, 35, 40, 28], [1, 4, 1, 2, 1, 0, 0]),
    ([22, 21, 20], [0, 0, 0]),
    ([22, 22, 22], [0, 0, 0]),
]


@pytest.mark.parametrize(param_names, param_values)
def test_daily_temperatures(benchmark, temperatures: List[int], expected: List[int]):
    solution = Solution()
    result = benchmark(solution.dailyTemperatures, temperatures)
    assert result == expected


@pytest.mark.parametrize(param_names, param_values)
def test_daily_temperatures2(benchmark, temperatures: List[int], expected: List[int]):
    solution = Solution()
    result = benchmark(solution.dailyTemperatures2, temperatures)
    assert result == expected

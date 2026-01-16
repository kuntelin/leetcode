import pytest
import logging
from typing import List
from collections import defaultdict

logger = logging.getLogger(__name__)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = {}
        for v in nums:
            nums_counter[v] = nums_counter.get(v, 0) + 1

        nums_frequent = sorted(nums_counter.items(), key=lambda item: item[1], reverse=True)
        logger.debug(f"{nums_frequent=}")

        return [k for k, v in nums_frequent[:k]]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        nums_counter = defaultdict(int)
        for v in nums:
            nums_counter[v] += 1

        nums_frequent = sorted(nums_counter.items(), key=lambda item: item[1], reverse=True)
        logger.debug(f"{nums_frequent=}")

        return [k for k, v in nums_frequent[:k]]


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 2, 3, 3, 3], 2, [3, 2]),
        ([7, 7], 1, [7]),
    ],
)
def test_top_k_frequent_elements(nums: List[int], k: int, expected: List[int]):
    solution = Solution()

    assert solution.topKFrequent(nums, k) == expected
    # assert solution.topKFrequent2(nums, k) == expected

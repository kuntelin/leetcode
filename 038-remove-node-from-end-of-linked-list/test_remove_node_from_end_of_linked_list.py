import logging
from typing import List, Optional

import pytest

from leetcode.list_node import (
    ListNode,
    from_list,
    to_list,
)

logger = logging.getLogger(__name__)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # 將所有節點快取到陣列中
        curr, cache = head, []
        while curr is not None:
            cache.append(curr)
            curr = curr.next

        # 找出要移除的位置
        idx = len(cache) - n

        # 位置在第一個，直接回傳第二個
        if idx == 0:
            return cache[0].next

        # 連結前一個與下一個節點
        cache[idx - 1].next = cache[idx].next

        return cache[0]


param_names = "head,n,expected"
param_values = [
    (
        [1, 2, 3, 4],
        2,
        [1, 2, 4],
    ),
    (
        [5],
        1,
        [],
    ),
    (
        [1, 2],
        2,
        [2],
    ),
]


@pytest.mark.parametrize(param_names, param_values)
def test_reorder_list(benchmark, head: List, n: int, expected: List):
    list_node_head = from_list(head)
    logger.debug(f"{to_list(list_node_head)=}")

    solution = Solution()
    result = benchmark(solution.removeNthFromEnd, list_node_head, n)

    logger.debug(f"{to_list(result)=}")

    assert to_list(result) == expected

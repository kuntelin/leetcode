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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        # * cache all node to list
        cache, curr = [], head
        while curr:
            cache.append(curr)
            curr = curr.next

        left, right = 0, len(cache) - 1
        while left < right:
            cache[left].next = cache[right]
            left += 1
            if left >= right:
                break
            cache[right].next = cache[left]
            right -= 1
        cache[left].next = None


param_names = "head,expected"
param_values = [
    (
        [0, 1, 2, 3, 4, 5, 6],
        [0, 6, 1, 5, 2, 4, 3],
    ),
    (
        [2, 4, 6, 8],
        [2, 8, 4, 6],
    ),
    (
        [2, 4, 6, 8, 10],
        [2, 10, 4, 8, 6],
    ),
]


@pytest.mark.parametrize(param_names, param_values)
def test_reorder_list(benchmark, head: List, expected: List):
    list_node_head = from_list(head)

    solution = Solution()
    benchmark(solution.reorderList, list_node_head)

    assert to_list(list_node_head) == expected

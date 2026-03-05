import logging
from typing import List, Optional

import pytest

from leetcode.node import (
    Node,
    from_list,
    to_list,
)

logger = logging.getLogger(__name__)


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        node_mapping = {None: None}
        curr = head
        while curr is not None:
            node_copy = Node(curr.val)
            node_mapping[curr] = node_copy
            curr = curr.next
        curr = head
        while curr is not None:
            node_copy = node_mapping.get(curr)
            node_copy.next = node_mapping.get(curr.next)
            node_copy.random = node_mapping.get(curr.random)
            curr = curr.next

        return node_mapping.get(head)


param_names = "head,expected"
param_values = [
    (
        [[3, None], [7, 3], [4, 0], [5, 1]],
        [[3, None], [7, 3], [4, 0], [5, 1]],
    ),
    (
        [[1, None], [2, 2], [3, 2]],
        [[1, None], [2, 2], [3, 2]],
    ),
]


@pytest.mark.parametrize(param_names, param_values)
def test_copy_test_with_random_pointer(benchmark, head: List, expected: List):
    node_head = from_list(head)

    solution = Solution()
    result = benchmark(solution.copyRandomList, node_head)
    result_list = result
    result_list = to_list(result)

    assert result_list == expected

import logging
from typing import List, Optional

import pytest

logger = logging.getLogger(__name__)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def dump_to_list(head: ListNode | None) -> List:
    if head is None:
        return []

    curr, result = head, []
    while curr is not None:
        result.append(curr.val)
        curr = curr.next

    return result


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev_node, curr_node = None, head
        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        return prev_node


param_names = "nums,expected"
param_values = [
    ([], []),
    ([1], [1]),
    ([0, 1, 2, 3], [3, 2, 1, 0]),
]


@pytest.mark.parametrize(param_names, param_values)
def test_reverse_linked_list(benchmark, nums: List, expected: List):
    # * convert nums to ListNode
    head, curr = None, None
    for num in nums:
        num_node = ListNode(val=num)
        if head is None:
            head = num_node
        else:
            # connect curr and next node
            curr.next = num_node

        # move curr to next node
        curr = num_node

    logger.debug(f"origin: {dump_to_list(head=head)=}")

    # * calculate the result
    solution = Solution()
    result = benchmark(solution.reverseList, head)

    logger.debug(f"result: {dump_to_list(head=result)=}")

    assert dump_to_list(result) == expected

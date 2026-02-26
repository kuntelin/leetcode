import logging
from typing import List, Optional

import pytest

logger = logging.getLogger(__name__)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_list_node(nums: List) -> None | ListNode:
    """
    * convert list to ListNode
    """

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

    return head


def dump_list_node(head: ListNode | None) -> List:
    """
    * convert ListNode to list
    """
    if head is None:
        return []

    curr, result = head, []
    while curr is not None:
        result.append(curr.val)
        curr = curr.next

    return result


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = ListNode()

        rev_head, rev_curr = temp_node, temp_node
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                rev_curr.next = curr1
                curr1 = curr1.next
            else:
                rev_curr.next = curr2
                curr2 = curr2.next
            rev_curr = rev_curr.next
        rev_curr.next = curr1 or curr2
        return rev_head.next


param_names = "list1,list2,expected"
param_values = [
    (
        [1, 2, 4],
        [1, 3, 5],
        [1, 1, 2, 3, 4, 5],
    ),
    (
        [],
        [1, 2],
        [1, 2],
    ),
    (
        [2],
        [1],
        [1, 2],
    ),
    (
        [5],
        [1, 2, 4],
        [1, 2, 4, 5],
    ),
]


@pytest.mark.parametrize(param_names, param_values)
def test_merge_two_sorted_linked_lists(
    benchmark,
    list1: List,
    list2: List,
    expected: List,
):
    list_node1 = generate_list_node(list1)
    logger.debug(f"{list1=}, {dump_list_node(list_node1)=}")
    list_node2 = generate_list_node(list2)
    logger.debug(f"{list2=}, {dump_list_node(list_node2)=}")

    solution = Solution()
    result = benchmark(solution.mergeTwoLists, list_node1, list_node2)

    logger.debug(f"{dump_list_node(result)=}")

    assert dump_list_node(result) == expected

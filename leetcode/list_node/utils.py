from typing import List

from .types import ListNode


def from_list(nums: List) -> None | ListNode:
    """
    * convert list to ListNode
    """
    if nums == []:
        return None

    dummy_head = curr = ListNode()
    for num in nums:
        node = ListNode(val=num)
        curr.next = node
        curr = curr.next

    return dummy_head.next


def to_list(head: ListNode | None) -> List:
    """
    * convert ListNode to list
    """
    if head is None:
        return []

    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result

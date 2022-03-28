import argparse
import logging
from typing import (
    List,
    Optional,
)

import pytest

from problems import TimeMethodMixin


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_linked_list(source: List) -> ListNode:
    head, pointer = None, None
    for item in source:
        node = ListNode(val=item, next=None)

        if head is None:
            # first item
            head = node
        else:
            # link to next
            pointer.next = node

        # move to next item
        pointer = node

    return head


def array_from_linked_list(source: ListNode) -> List:
    if source is None:
        return []

    values = []
    while source:
        values.append(source.val)
        source = source.next

    return values


def print_linked_list(head: ListNode) -> None:
    msg = ''
    msg += 'head -> '
    while head.next is not None:
        msg += f"{head.val} -> "
        head = head.next
    msg += f"{head.val} "
    msg += '-> tail'
    logging.debug(f'linked_list: {msg}')


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> [Optional[ListNode], List]:
        return self.array_sorted(lists)
        # return self.merge_two_list(lists)
        pass

    def array_sorted(self, lists: List[Optional[ListNode]]) -> [Optional[ListNode], List]:
        # empty list
        if lists == [] or all(map(lambda x: x == [], lists)):
            return None

        values = []
        for joined_list in lists:
            while joined_list is not None:
                values.append(joined_list.val)
                joined_list = joined_list.next

        head, pointer = None, None
        for item in sorted(values):
            if head is None:
                head = ListNode(val=item)
                pointer = head
            else:
                pointer.next = ListNode(val=item)
                pointer = pointer.next

        return head

    def merge_two_list(self, lists: List[Optional[ListNode]]) -> [Optional[ListNode], List]:
        # filter empty items
        cleaned_lists = list(filter(lambda x: x is not None and x != [], lists))

        # empty list
        if not cleaned_lists:
            return None

        def _merge_list(list1, list2):
            head, pointer = None, None
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    if head is None:
                        # set head node
                        head = list1
                    else:
                        # link previous node
                        pointer.next = list1

                    # move forward
                    pointer = list1
                    list1 = list1.next
                else:
                    if head is None:
                        # set head node
                        head = list2
                    else:
                        # link previous node
                        pointer.next = list2

                    # move forward
                    pointer = list2
                    list2 = list2.next

                # list1 is empty
                if list1 is None:
                    pointer.next = list2

                # list2 is empty
                if list2 is None:
                    pointer.next = list1

            return head

        final_head = None
        logging.debug(f'{cleaned_lists=}')
        for joined_list in cleaned_lists:
            if final_head is None:
                final_head = joined_list
            else:
                final_head = _merge_list(final_head, joined_list)

        return final_head


class TestSolution(TimeMethodMixin):
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["lists", "result"],
        [
            ([], []),
            ([[]], []),
            ([array_to_linked_list([1, 4, 5]), array_to_linked_list([1, 3, 4]), array_to_linked_list([2, 6])], [1, 1, 2, 3, 4, 4, 5, 6]),
            ([array_to_linked_list([2]), array_to_linked_list([]), array_to_linked_list([-1])], [-1, 2]),
        ],
    )
    def test_answer(self, lists, result):
        logging.debug('execute function')
        response = self.time_method(self.solution.mergeKLists, *(lists, ), **{})

        logging.debug('compare output')
        assert array_from_linked_list(response) == result

    def teardown_method(self, method):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-cli-level', action='store', type=str.upper, default='WARNING')
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.getLevelName(args.log_cli_level))


if __name__ == '__main__':
    main()

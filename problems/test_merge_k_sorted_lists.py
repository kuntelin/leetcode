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


def to_linked_list(source: List) -> ListNode:
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


def from_linked_list(source: ListNode) -> List:
    return []


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
        # empty list
        if lists == [] or all(map(lambda x: x == [], lists)):
            return []

        head, pointer = None, None
        for idx, joined_list in enumerate(lists):
            logging.info(f'process item {idx}, {joined_list}')

            if head is None:
                head = joined_list

        raise Exception('not finished')


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
            ([to_linked_list([1, 4, 5]), to_linked_list([1, 3, 4]), to_linked_list([2, 6])], [1, 1, 2, 3, 4, 4, 5, 6]),
        ],
    )
    def test_answer(self, lists, result):
        logging.debug('execute function')
        response = self.time_method(self.solution.mergeKLists, *(lists, ), **{})

        logging.debug('compare output')
        assert response == result

    def teardown_method(self, method):
        pass


def main():
    parser = argparse.ArgumentParser()
    loglevel_exclusive_group = parser.add_mutually_exclusive_group()
    # loglevel_exclusive_group.add_argument(
    #     '-v', '--verbose',
    #     action='store_const', type=int, dest='loglevel', default=logging.WARNING, const=logging.INFO,
    #     help='Enable verbose mode',
    # )
    # loglevel_exclusive_group.add_argument(
    #     '-d', '--debug',
    #     action='store_const', type=int, dest='loglevel', default=logging.WARNING, const=logging.DEBUG,
    #     help='Enable debug mode',
    # )
    parser.add_argument('--log-cli-level', action='store', type=str.upper, default='WARNING')
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.getLevelName(args.log_cli_level))

    logging.info('info message')
    logging.debug('debug message')
    # print_linked_list(
    #     ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))
    # )
    print_linked_list(to_linked_list([1, 3, 5, 7, 9]))


if __name__ == '__main__':
    main()

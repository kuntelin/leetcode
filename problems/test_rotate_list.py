import argparse
import logging
import time

import pytest

from .utils import (
    ListNode,
    list_nodes_to_array,
    array_to_list_nodes,
)


class Solution1:
    """
    using python array
    """
    @staticmethod
    def get_node_count(head):
        if head is None:
            return 0
        else:
            node_len = 1
            curt_node = head
            while curt_node.next is not None:
                curt_node = curt_node.next
                node_len += 1
            return node_len

    @staticmethod
    def move_last_to_first(head):
        # walk to last node
        curt_node = head
        prev_node = None
        while curt_node.next is not None:
            prev_node = curt_node
            curt_node = curt_node.next

        if prev_node is None:
            # only one node
            new_head = curt_node
        else:
            # nodes more than one
            new_head = curt_node
            new_head.next = head
            prev_node.next = None

        return new_head

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # no nodes, return head
        if head is None:
            return head

        # get node length
        node_len = self.get_node_count(head)
        logging.debug(f'{node_len=}')

        # reduce loop number
        if k >= node_len:
            one_round = k % node_len
        else:
            one_round = k
        logging.debug(f'{one_round=}')

        # the same order
        if one_round == 0:
            return head

        # move last node to first recursively
        while one_round > 0:
            head = self.move_last_to_first(head)
            one_round -= 1

        return head


class Solution2:
    """
    using python array
    """
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        # count list length
        head_array = list_nodes_to_array(head)
        head_len = len(head_array)

        if k >= head_len:
            k = k % head_len

        # the same order
        if k == 0:
            return head

        result = head_array[-k:] + head_array[:(head_len - k)]

        return array_to_list_nodes(result)


class TestSolution:
    def setup_class(self):
        # self.solution = Solution1()
        self.solution = Solution2()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @staticmethod
    def time_method(func, *args, **kwargs):
        t1 = time.perf_counter()

        response = None
        except_instance = None
        try:
            response = func(*args, **kwargs)
        except Exception as e:
            except_instance = e
        t2 = time.perf_counter()

        logging.info(f'Execution in {(t2 - t1)} seconds')

        if except_instance is not None:
            raise except_instance

        return response

    @pytest.mark.parametrize(
        ["head", "k", "result"],
        [
            ([0, 1, 2], 1, [2, 0, 1]),
            ([0, 1, 2], 2, [1, 2, 0]),
            ([0, 1, 2], 3, [0, 1, 2]),
            ([0, 1, 2], 4, [2, 0, 1]),
            ([1], 1, [1]),
            ([1, 2, 3], 2000000000, [2, 3, 1]),
        ],
    )
    @pytest.mark.benchmark
    def test_rotateRight(self, benchmark, head, k, result):
        logging.info(f'testing: {head=}, {k=}, {result=}')

        logging.debug('convert input')
        head = array_to_list_nodes(head)

        logging.debug('execute function')
        response = benchmark(self.solution.rotateRight, *(head, k), **{})

        logging.debug('compare output')
        assert list_nodes_to_array(response) == result

    def teardown_method(self, method):
        pass


def main():
    parser = argparse.ArgumentParser()
    exclusive_group = parser.add_mutually_exclusive_group()
    exclusive_group.add_argument('--verbose', action='store_true')
    exclusive_group.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)
    elif args.debug:
        logging.getLogger().setLevel(logging.DEBUG)


if __name__ == '__main__':
    main()

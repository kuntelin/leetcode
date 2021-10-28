import argparse
import logging
import time

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_list_nodes(data) -> [ListNode, None]:
    """
    convert array to list
    [] = None
    [1, 2, 3, 4, 8] = ListNode(1) -> ListNode(2) -> ListNode(3) -> ListNode(4) -> ListNode(8)
    """

    if data is []:
        return None
    else:
        head = None
        prev = None
        for item in data:
            current = ListNode(val=item)

            if head is None and prev is None:
                head = current
            elif head is not None and prev is None:
                head.next = current
                prev = current
            else:
                prev.next = current
                prev = current

        return head


def list_nodes_to_array(head) -> list:
    """
    convert list to array
    None = []
    ListNode(1) -> ListNode(2) -> ListNode(3) -> ListNode(4) -> ListNode(8) = [1, 2, 3, 4, 8]
    """
    data = []
    while head is not None:
        data.append(head.val)
        head = head.next
    return data


class Solution:
    @staticmethod
    def add_node(l1_node, l2_node, ten_val):
        if l1_node is None:
            l1_val = 0
        else:
            l1_val = l1_node.val

        if l2_node is None:
            l2_val = 0
        else:
            l2_val = l2_node.val

        ten_val, val = divmod((l1_val + l2_val + ten_val), 10)

        return ListNode(val), ten_val

    def addTwoNumbers(self, l1, l2) -> ListNode:
        result_head = None
        previous_node = None
        ten_val = 0
        while not (l1 is None and l2 is None and ten_val == 0):
            new_node, ten_val = self.add_node(l1, l2, ten_val)

            if result_head is None:
                # set first node
                result_head = new_node
            else:
                # link previous node and new node
                previous_node.next = new_node

            # move to next node
            previous_node = new_node
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return result_head


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
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
        ["l1", "l2", "result"],
        [
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ([0], [0], [0]),
            ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ]
    )
    def test_rotateRight(self, l1, l2, result):
        logging.info(f'testing: {l1=}, {l2=}, {result=}')

        logging.debug('convert input')
        l1 = array_to_list_nodes(l1)
        l2 = array_to_list_nodes(l2)

        logging.debug('execute function')
        response = self.time_method(self.solution.addTwoNumbers, *(l1, l2), **{})

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

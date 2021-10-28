import argparse
import logging

import pytest

from .utils import (
    ListNode,
    array_to_list_nodes,
    list_nodes_to_array,
    array_to_bi_direction_link_list,
    debug_bi_direction_link_list,
)


class Solution:
    """
    using python array
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> [ListNode, None]:
        data_array = list_nodes_to_array(head)
        data_len = len(data_array)
        logging.debug(f'{data_array=}, {data_len=}')

        if data_len == 0:
            return head

        if n <= 0 or n > data_len:
            return head

        if data_len == 1 and n == 1:
            return None

        remove_idx = data_len - n
        if (remove_idx - 1) < 0:
            result = data_array[1:]
        elif (remove_idx + 1) >= data_len:
            result = data_array[:-1]
        else:
            result = data_array[0:remove_idx] + data_array[remove_idx + 1:]

        return array_to_list_nodes(result)


class Solution2:
    """
    using link list
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> [ListNode, None]:
        # get list length
        data_len = 0
        tmp_head = head
        while tmp_head is not None:
            data_len += 1
            tmp_head = tmp_head.next
        logging.debug(f'{data_len=}')

        if data_len == 0:
            return head

        if n <= 0 or n > data_len:
            return head

        if data_len == 1 and n == 1:
            return None

        target_node = data_len - n + 1
        if target_node == 1:
            # remove item is first item
            return head.next

        tmp_head = head
        prev = None
        while tmp_head is not None:
            target_node -= 1

            if target_node == 0:
                # remove this node

                if tmp_head.next is None:
                    # end of the list
                    prev.next = None
                else:
                    # set link
                    prev.next = tmp_head.next

                    # move to next
                    prev = tmp_head.next
                    tmp_head = tmp_head.next.next
            else:
                # move to next
                prev = tmp_head
                tmp_head = tmp_head.next

        return head


class Solution3:
    """
    using bi direction link list
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> [ListNode, None]:
        list_len, list_head = array_to_bi_direction_link_list(list_nodes_to_array(head))
        target_idx = list_len - n + 1

        logging.debug(f'{list_len=}, {list_head=}, {target_idx=}')

        if list_len == 0:
            return list_head

        if n <= 0 or n > list_len:
            return list_head

        if list_len == 1 and n == 1:
            return None

        if target_idx == 1:
            # remove first item
            return list_head.next

        logging.debug('before remove')
        debug_bi_direction_link_list(list_head)

        # walk through list and remove target_idx
        tmp_head = list_head
        while tmp_head is not None:
            if tmp_head.index == target_idx:
                # remove this node
                if tmp_head.prev is None:
                    tmp_head.next.prev = None
                    tmp_head = tmp_head.next
                elif tmp_head.next is None:
                    tmp_head.prev.next = None
                    tmp_head = None
                else:
                    tmp_head.prev.next = tmp_head.next
                    tmp_head.next.prev = tmp_head.prev
                    tmp_head = tmp_head.next
            else:
                # not this node, go to next
                tmp_head = tmp_head.next

        logging.debug('after remove')
        debug_bi_direction_link_list(list_head)

        return list_head


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        # self.solution = Solution2()
        # self.solution = Solution3()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["data", "remove_nth", "result"],
        [
            ([1], -1, [1]),
            ([1], 0, [1]),
            ([1], 1, []),
        ]
    )
    def test_positive(self, data, remove_nth, result):
        logging.info(f'testing: {data=}, {remove_nth=}, {result=}')
        assert list_nodes_to_array(self.solution.removeNthFromEnd(array_to_list_nodes(data), remove_nth)) == result

    @pytest.mark.parametrize(
        ["data", "remove_nth", "result"],
        [
            ([], -1, []),
            ([], 0, []),
            ([], 1, []),
        ]
    )
    def test_empty_list(self, data, remove_nth, result):
        logging.info(f'testing: {data=}, {remove_nth=}, {result=}')
        assert list_nodes_to_array(self.solution.removeNthFromEnd(array_to_list_nodes(data), remove_nth)) == result

    @pytest.mark.parametrize(
        ["data", "remove_nth", "result"],
        [
            ([1], 2, [1]),
            ([1, 2], 3, [1, 2]),
            ([1, 2, 3], 4, [1, 2, 3]),
        ]
    )
    def test_out_of_bound(self, data, remove_nth, result):
        logging.info(f'testing: {data=}, {remove_nth=}, {result=}')
        assert list_nodes_to_array(self.solution.removeNthFromEnd(array_to_list_nodes(data), remove_nth)) == result

    @pytest.mark.parametrize(
        ["data", "remove_nth", "result"],
        [
            ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
            ([1], 1, []),
            ([1, 2], 1, [1]),
            ([1, 2], 2, [2]),
        ]
    )
    def test_all(self, data, remove_nth, result):
        logging.info(f'testing: {data=}, {remove_nth=}, {result=}')
        assert list_nodes_to_array(self.solution.removeNthFromEnd(array_to_list_nodes(data), remove_nth)) == result


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

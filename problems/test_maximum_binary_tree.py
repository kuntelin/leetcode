import logging
from typing import (
    Optional,
    List,
)

import pytest

from problems.utils import (
    TreeNode,
    tree_node_from_list,
    tree_node_to_list,
)


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not 1 <= len(nums) <= 1000:
            raise ValueError

        if any(map(lambda x: not 0 <= x <= 1000, nums)):
            raise ValueError

        if len(nums) != len(set(nums)):
            raise ValueError

        def _find_max_index(items):
            # max_value, max_index = -1, -1
            # for index, item in enumerate(items):
            #     if item > max_value:
            #         max_value = item
            #         max_index = index
            #
            # return max_index
            return items.index(max(items))

        def _construct_children(node_values) -> Optional[TreeNode]:
            node_length = len(node_values)

            if node_length == 0:
                return None

            if node_length == 1:
                return TreeNode(node_values[0])

            max_index = _find_max_index(node_values)

            node_object = TreeNode(node_values[max_index])

            left_values = node_values[:max_index]
            if left_values:
                node_object.left = _construct_children(left_values)

            right_values = node_values[max_index + 1:]
            if right_values:
                node_object.right = _construct_children(right_values)

            return node_object

        # using copy of nums instead of change the nums values
        return _construct_children(nums[:])


class TestSolution:
    def setup_class(self):
        self.solution = Solution()

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["node_list"],
        [
            ([6, 3, 5, None, 2, 0, None, None, 1], ),
        ]
    )
    def test_tree_node_help_functions(self, node_list):
        logging.debug(f'{node_list=}')
        assert tree_node_to_list(tree_node_from_list(node_list)) == node_list

    @pytest.mark.parametrize(
        ["nums", "result"],
        [
            ([3, 2, 1, 6, 0, 5], [6, 3, 5, None, 2, 0, None, None, 1]),
        ],
    )
    @pytest.mark.benchmark
    def test_constructMaximumBinaryTree(self, nums, result):  # noqa
        logging.debug(f'{nums=}, {result=}')
        assert tree_node_to_list(self.solution.constructMaximumBinaryTree(nums)) == result

    def teardown_method(self, method):
        pass

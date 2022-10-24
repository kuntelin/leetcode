import argparse
import logging

import pytest

from typing import (
    Optional,
    Union,
    List,
)
from problems.utils import (
    TreeNode,
)
from collections import defaultdict


def list_to_tree(children_values):
    if children_values is None or len(children_values) == 0:
        return None

    root_node = TreeNode(val=children_values[0])

    # recursive build tree
    construct_children([root_node], children_values[1:].copy())

    return root_node


def construct_children(parent_nodes, children_values):
    if not isinstance(parent_nodes, list):
        raise ValueError

    if len(parent_nodes) == 0:
        return None

    children_nodes = []
    children_values_copy = children_values.copy()
    for parent_node in parent_nodes:
        logging.debug(f'construct_children::parent_node.val = {parent_node.val}')

        # if the parent is TreeNode(val=None), then it won't have child, by pass it
        if parent_node.val is None:
            continue

        try:
            left_node = TreeNode(val=children_values_copy.pop(0))

            parent_node.left = left_node
            children_nodes.append(left_node)

            logging.debug(f'{parent_node.val} -> left is {left_node.val}')
        except IndexError:
            pass

        try:
            right_node = TreeNode(val=children_values_copy.pop(0))

            parent_node.right = right_node
            children_nodes.append(right_node)

            logging.debug(f'{parent_node.val} -> right is {right_node.val}')
        except IndexError:
            pass

    if children_nodes:
        construct_children(children_nodes, children_values_copy)


def tree_to_list(root: Union[None, TreeNode]) -> List:
    if root is None:
        return []
    else:
        return nodes_to_list([root])


def nodes_to_list(nodes: List[TreeNode]):
    node_values = []
    children_nodes = []
    for node in nodes:
        node_values.append(node.val)

        if node.left is not None:
            children_nodes.append(node.left)

        if node.right is not None:
            children_nodes.append(node.right)

    if children_nodes:
        node_values.extend(nodes_to_list(children_nodes))

    return node_values


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        summary = defaultdict(lambda: 0)

        def travel_nodes(level, node):
            current_level = level + 1

            logging.info(f'{current_level=}, {node.val=}, {node.left=}, {node.right=}')

            if node is None or node.val is None:
                return None

            if node.left is not None:
                travel_nodes(current_level, node.left)

            if node.right is not None:
                travel_nodes(current_level, node.right)

            if node.left is None and node.right is None:
                summary[current_level] += node.val
            elif node.left and node.left.val is None and node.right and node.right.val is None:
                summary[current_level] += node.val

        travel_nodes(0, root)

        logging.info(f'{summary=}')

        return summary[max(summary.keys())]


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["nodes", "deepest_sum"],
        [
            ([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8], 15),
            ([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], 19),
            ([], 0),
        ],
    )
    @pytest.mark.benchmark
    def test_deepest_leaves_sum(self, nodes, deepest_sum):
        root = list_to_tree(nodes)
        logging.debug(f'{tree_to_list(root)=}')
        assert nodes == tree_to_list(root)
        assert self.solution.deepestLeavesSum(root) == deepest_sum

    @pytest.mark.parametrize(
        ["nodes"],
        [
            ([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8], ),
            ([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], ),
            ([], ),
        ],
    )
    @pytest.mark.benchmark
    def test_build_tree_and_expose_tree_are_the_same(self, nodes):
        root = list_to_tree(nodes)
        assert nodes == tree_to_list(root)

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

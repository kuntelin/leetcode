import argparse
import logging
from collections import defaultdict
from typing import Optional, List

import pytest

from problems.utils import TreeNode, tree_node_from_list


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # noqa
        if root is None:
            return []

        level_items = defaultdict(list)

        def flood(node, level):
            level_items[level].append(node.val)

            if node.left is None and node.right is None:
                return

            if node.left:
                flood(node.left, level + 1)

            if node.right:
                flood(node.right, level + 1)

        flood(root, 0)
        # logging.debug(level_items)

        return [x for x in level_items.values()]


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["root", "result"],
        [
            ([], []),
            ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
            ([1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]]),
        ]
    )
    def test_level_order(self, root, result):
        logging.info(f'testing: {root=}, {result=}')
        root_node = tree_node_from_list(root)
        assert self.solution.levelOrder(root_node) == result


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

    pass


if __name__ == '__main__':
    main()

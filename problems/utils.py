import argparse
import logging
from typing import Union, List
from collections import defaultdict


__all__ = [
    'ListNode',
    'BiDirectListNode',
    'TreeNode',
    'echo',
    'list_node_to_list',
    'list_node_from_list',
    'bi_direction_link_list_from_list',
    'bi_direction_link_list_debug',
    'tree_node_from_list',
    'tree_node_to_list',
]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class BiDirectListNode:
    def __init__(self, val=0, index=None, prev=None, next=None):
        self.val = val
        self.index = index
        self.prev = prev
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def echo(arg):
    return arg


def list_node_to_list(list_head):
    """
    convert list to array
    None = []
    ListNode(1) -> ListNode(2) -> ListNode(3) -> ListNode(4) -> ListNode(8) = [1, 2, 3, 4, 8]
    """
    array_data = []
    while list_head is not None:
        array_data.append(list_head.val)
        list_head = list_head.next
    return array_data


def list_node_from_list(data) -> [ListNode, None]:
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


def bi_direction_link_list_from_list(array_data) -> (int, [BiDirectListNode, None]):
    if array_data is []:
        return 0, None
    else:
        counter = 0
        head = None
        prev = None
        idx = 0
        for item in array_data:
            counter += 1
            idx += 1
            current = BiDirectListNode(item, idx)

            if head is None and prev is None:
                head = current
            elif head is not None and prev is None:
                prev = head

                # make bi-direction link
                prev.next = current
                current.prev = prev

                # move to next
                prev = current
            else:
                # make bi-direction link
                prev.next = current
                current.prev = prev

                # move to next
                prev = current
        return counter, head


def bi_direction_link_list_debug(list_head: [BiDirectListNode, None]):
    # walk through bi direction link list
    walk_head = list_head

    logging.debug('-' * 80)

    msg = ''
    msg += 'None <-'
    while walk_head is not None:
        # current
        msg += f' {walk_head.val} '

        walk_head = walk_head.next
    msg += '-> None'
    logging.debug(f'{msg}')

    logging.debug('=' * 80)


def tree_node_from_list(tree_nodes: List[int]) -> Union[TreeNode, None]:
    if not tree_nodes:
        return None

    def item_number_in_depth(_depth: int) -> int:
        return 2 ** (_depth - 1)

    def total_item_number_in_depth(_depth: int) -> int:
        return sum([item_number_in_depth(d) for d in range(1, _depth + 1)])

    def find_depth(dest_number) -> (int, int):
        _depth, _item_number = 1, total_item_number_in_depth(1)
        while dest_number > _item_number:
            _depth += 1
            _item_number = total_item_number_in_depth(_depth)
        return _depth, _item_number

    def construct_children(parent_nodes: List[TreeNode], children_values: List):
        children_nodes = []
        for parent_node in parent_nodes:
            left_val = children_values.pop(0)
            if left_val is not None:
                left_node = TreeNode(left_val)
                children_nodes.append(left_node)
                parent_node.left = left_node

            right_val = children_values.pop(0)
            if right_val is not None:
                right_node = TreeNode(right_val)
                children_nodes.append(right_node)
                parent_node.right = right_node

        if children_nodes:
            logging.debug(f'{children_values=}')
            construct_children(children_nodes, children_values)

    node_counter = len(tree_nodes)

    if node_counter == 0:
        return None
    elif node_counter == 1:
        return TreeNode(tree_nodes.pop(0))
    else:
        depth, expected_node_counter = find_depth(node_counter)
        logging.info(f'expected depth {depth} have {expected_node_counter} items in it')

        if node_counter != expected_node_counter:
            tree_nodes.extend([None] * (expected_node_counter - node_counter))

        logging.info(f'tree_nodes now have {len(tree_nodes)} items in it')
        logging.debug(f'{tree_nodes=}')

        root = TreeNode(tree_nodes.pop(0))

        construct_children([root], tree_nodes)

        return root


def tree_node_to_list(root: TreeNode) -> List[int]:
    def expose_children(tree_node, depth, total_values):
        if tree_node is None:
            total_values[depth].append(None)
            return

        total_values[depth].append(tree_node.val)

        if tree_node.left is None and tree_node.right is None:
            return

        expose_children(tree_node.left, depth + 1, total_values)
        expose_children(tree_node.right, depth + 1, total_values)

    result = defaultdict(list)
    expose_children(root, 0, result)

    logging.debug(f'{result=}')

    final_value = []
    for values in result.values():
        if all(map(lambda x: x is None, values)):
            # skip all None values
            continue
        final_value.extend(values)
    logging.debug(f'{final_value=}')

    return final_value


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

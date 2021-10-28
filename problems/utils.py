import argparse
import logging


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


def list_to_array(list_head):
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


def array_to_list(array_data):
    """
    convert array to list
    [] = None
    [1, 2, 3, 4, 8] = ListNode(1) -> ListNode(2) -> ListNode(3) -> ListNode(4) -> ListNode(8)
    """

    if array_data is []:
        return None
    else:
        head = None
        prev = None

        for item in array_data:
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


def array_to_link_list(array_data) -> (int, [ListNode, None]):
    """
    convert array to list
    [] = None
    [1, 2, 3, 4, 8] = ListNode(1) -> ListNode(2) -> ListNode(3) -> ListNode(4) -> ListNode(8)
    """

    if array_data is []:
        return 0, None
    else:
        counter = 0
        head = None
        prev = None

        for item in array_data:
            counter += 1
            current = ListNode(val=item)

            if head is None and prev is None:
                head = current
            elif head is not None and prev is None:
                head.next = current
                prev = current
            else:
                prev.next = current
                prev = current

        return counter, head


def array_to_bi_direction_link_list(array_data) -> (int, [BiDirectListNode, None]):
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


def debug_bi_direction_link_list(list_head: [BiDirectListNode, None]):
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

    print(list_to_array(array_to_list([])))
    print(list_to_array(array_to_list([1, 2, 3, 4, 8])))


if __name__ == '__main__':
    main()

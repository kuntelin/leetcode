import logging
from typing import List

from .types import Node

__all__ = [
    "from_list",
    "to_list",
]

logger = logging.getLogger(__name__)


def from_list(nums: List) -> None | Node:
    if nums == []:
        return None

    # 建立快取字典
    node_cache = {}

    # 建立所有Node
    for idx, data in enumerate(nums):
        node_cache[idx] = Node(data[0])

    # 連結next及random
    for idx, data in enumerate(nums):
        node_cache[idx].next = node_cache.get(idx + 1, None)
        node_cache[idx].random = node_cache.get(data[1], None)

    logger.debug(f"{node_cache=}")

    return node_cache[0]


def to_list(head: Node | None) -> List:
    if head is None:
        return []

    # 記錄每個Node及其索引值
    node_mapping = {}

    # 記錄最終結果
    result = []

    curr, idx = head, 0
    while curr:
        node_mapping[curr] = idx
        curr = curr.next
        idx += 1

    curr = head
    while curr:
        result.append([curr.val, node_mapping.get(curr.random, None)])
        curr = curr.next

    logger.debug(f"{result=}")

    return result

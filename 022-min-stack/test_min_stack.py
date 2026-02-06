import logging
import math
from typing import List

import pytest

logger = logging.getLogger(__name__)


class MinStack:
    def __init__(self):
        self.cache = []

    def push(self, val: int) -> None:
        self.cache.append(val)

    def pop(self) -> None:
        self.cache.pop()

    def top(self) -> int:
        return self.cache[-1]

    def getMin(self) -> int:
        min_val = math.inf
        for idx in range(len(self.cache)):
            min_val = min(min_val, self.cache[idx])

        return min_val


param_names = "actions,expected"
param_values = [
    (
        ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"],
        [None, None, None, None, 0, None, 2, 1],
    ),
]


@pytest.mark.parametrize(param_names, param_values)
def test_min_stack(actions: List[str | int], expected: List[None | int]):
    min_stack: None | MinStack = None
    idx, ans = 0, []
    while idx < len(actions):
        action = actions[idx]
        if action == "MinStack":
            logger.info("initialize MinStack")

            min_stack = MinStack()
            ans.append(None)
        elif action == "push":
            logger.info(f"calling {action=}")

            idx += 1
            val = actions[idx]
            rtn = min_stack.push(val)

            ans.append(rtn)
        else:
            logger.info(f"calling {action=}")

            func = getattr(min_stack, action)
            rtn = func()
            logger.debug(f"{action=}, {rtn=}")

            ans.append(rtn)

        idx += 1

    assert ans == expected

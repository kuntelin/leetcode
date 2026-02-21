import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class TimeMap:
    def __init__(self):
        self._cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._cache:
            self._cache[key] = []
        self._cache[key].append((timestamp, value))
        logger.debug(f"{self._cache=}")

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._cache:
            return ""

        target = None
        for t, v in self._cache[key]:
            logger.debug(f"{t=}, {v=}")

            if t <= timestamp:
                target = v

        return target if target is not None else ""

        logger.debug(f"{self._cache[key]=}")


param_names = "actions,expected"
param_values = [
    (
        [
            "TimeMap",
            "set",
            ["alice", "happy", 1],
            "get",
            ["alice", 1],
            "get",
            ["alice", 2],
            "set",
            ["alice", "sad", 3],
            "get",
            ["alice", 3],
        ],
        [None, None, "happy", "happy", None, "sad"],
    ),
    (
        ["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]],
        [None, None, "", "value1", "value1"],
    ),
]


@pytest.mark.parametrize(param_names, param_values)
def test_search_in_rotated_sorted_array(benchmark, actions: List[str | List[str | int]], expected: List[None | str]):
    i = 0
    ins: TimeMap = None
    result = []
    while i < len(actions):
        logger.debug(f"{actions[i]=}")
        if actions[i] == "TimeMap":
            ins = TimeMap()
            result.append(None)
        elif actions[i] == "set":
            i += 1
            k, v, t = actions[i]
            result.append(ins.set(key=k, value=v, timestamp=t))
        elif actions[i] == "get":
            i += 1
            k, t = actions[i]
            result.append(ins.get(key=k, timestamp=t))
        else:
            logger.debug("?" * 30)

        i += 1

    assert result == expected

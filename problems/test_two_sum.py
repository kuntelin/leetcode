import argparse
import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, val in enumerate(nums):
            diff_idx = cache.get(target - val, None)

            if diff_idx is not None:
                return [diff_idx, idx]

            cache[val] = idx


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["nums", "target", "result"],
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ],
    )
    def test_minimumTotal(self, nums: List[int], target: int, result: List[int]):
        assert self.solution.twoSum(nums, target) == result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log-cli-level", action="store", type=str.upper, default="WARNING"
    )
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.getLevelName(args.log_cli_level))


if __name__ == "__main__":
    main()

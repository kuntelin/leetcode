import argparse
import logging
import pytest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        if not 2 <= n <= 10 ** 5:
            raise ValueError

        if any(map(lambda x: not 0 <= x <= 10 ** 4, height)):
            raise ValueError

        max_area = 0
        left_idx, right_idx = 0, n - 1
        while left_idx < right_idx:
            left_height, right_height = height[left_idx], height[right_idx]
            max_area = max(
                max_area,
                min(left_height, right_height) * (right_idx - left_idx),
            )
            if left_height > right_height:
                right_idx = right_idx - 1
            else:
                left_idx = left_idx + 1

        return max_area


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ['input_data', 'output_result'],
        [
            ([-1, 10, 10 ** 4], 0),
            ([0, 10, 10 ** 4 + 1], 0),
        ]
    )
    def test_out_of_bound(self, input_data, output_result):
        with pytest.raises(ValueError):
            self.solution.maxArea(input_data)

    @pytest.mark.parametrize(
        ["input_data", "output_result"],
        [
            ([1, 1], 1),
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),

        ],
    )
    def test_maxArea(self, input_data, output_result):
        assert self.solution.maxArea(input_data) == output_result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-cli-level', action='store', type=str.upper, default='WARNING')
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.getLevelName(args.log_cli_level))


if __name__ == '__main__':
    main()

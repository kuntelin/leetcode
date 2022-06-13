import argparse
import logging
import pytest
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row_idx in range(1, len(triangle)):
            for col_idx in range(len(triangle[row_idx])):
                if col_idx == 0:
                    # set minimum total to parent in the first item
                    minimum_total = triangle[row_idx - 1][col_idx]
                elif col_idx == row_idx:
                    # set minimum total to parent in the last item
                    minimum_total = triangle[row_idx - 1][col_idx - 1]
                else:
                    # set minimum total to compare from two parent
                    minimum_total = min(
                        triangle[row_idx - 1][col_idx - 1],
                        triangle[row_idx - 1][col_idx],
                    )

                # set the minimum total to current item
                triangle[row_idx][col_idx] += minimum_total

        return min(triangle[-1])


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["input_data", "output_result"],
        [
            ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
            # ([[-10]], -10),
            # ([[-1], [2, 3], [1, -1, -3]], -1),
        ],
    )
    def test_minimumTotal(self, input_data, output_result):
        assert self.solution.minimumTotal(input_data) == output_result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-cli-level', action='store', type=str.upper, default='WARNING')
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.getLevelName(args.log_cli_level))


if __name__ == '__main__':
    main()

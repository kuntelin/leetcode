import argparse
import logging

import pytest


class Solution1:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sum_list = sorted(nums1 + nums2)
        logging.debug(f'{sum_list=}')
        sum_len = len(sum_list)

        if (sum_len % 2) == 0:
            logging.debug(f'target index => {int(sum_len / 2)}')
            sum1 = sum_list[int(sum_len / 2) - 1]
            logging.debug(f'{sum1=}')
            sum2 = sum_list[int(sum_len / 2)]
            logging.debug(f'{sum2=}')
            result = (float(sum1) + float(sum2)) / 2
        else:
            result = float(sum_list[int(sum_len / 2)])

        return result


class Solution2:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sum_list = sorted(nums1 + nums2)
        quotient, remainder = divmod(len(sum_list), 2)

        if remainder == 0:
            result = float(sum_list[quotient - 1] + sum_list[quotient]) / 2
        else:
            result = float(sum_list[quotient])

        return result


class TestSolution:
    def setup_class(self):
        # self.solution = Solution1()
        self.solution = Solution2()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.parametrize(
        ['num1', 'num2', 'result'],
        [
            ([], [1], 1.0),
            ([2], [], 2.0),
            ([1, 3], [2], 2.0),
        ]
    )
    def test_different_size(self, num1, num2, result):
        logging.info(f'testing: {num1=}, {num2=}, {result=}')
        assert self.solution.findMedianSortedArrays(num1, num2) == result

    @pytest.mark.parametrize(
        ['num1', 'num2', 'result'],
        [
            ([1, 2], [3, 4], 2.5),
            ([1, 3], [2, 7], 2.5),
            ([0, 0], [0, 0], 0.0),
        ]
    )
    def test_same_size(self, num1, num2, result):
        logging.info(f'testing: {num1}, {num2}, {result}')
        assert self.solution.findMedianSortedArrays(num1, num2) == result


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

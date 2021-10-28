import argparse
import logging

import pytest


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def is_palindromic(num: str) -> bool:
            logging.info(f'checking {num} is_palindromic')

            num_len = len(num)

            if num_len == 1:
                return True

            if (len(num) % 2) == 0:
                middle_idx = int((num_len + 1) / 2)
            else:
                middle_idx = int(num_len / 2)
            logging.debug(f'middle_idx is {middle_idx}')

            palindromic = False
            for i in range(1, middle_idx + 1):
                logging.debug(f'num[{i-1}] = {num[i - 1]}, num[{-i}] = {num[-i]}')
                if num[i - 1] != num[-i]:
                    return False
                else:
                    palindromic = True
            return palindromic

        num_min = 1
        num_max = 10 ** 18 - 1

        if len(n) == 1 and (num_min <= int(n) <= num_max):
            return str(int(n) - 1)

        int_num = int(n)
        diff_val = 1
        smaller_over_boundary = False
        larger_over_boundary = False
        while not smaller_over_boundary and not larger_over_boundary:
            # smaller
            temp_num = int_num - diff_val
            smaller_over_boundary = not (num_min <= temp_num <= num_max)
            if not smaller_over_boundary:
                if is_palindromic(str(int_num - diff_val)):
                    return str(int_num - diff_val)

            # larger
            temp_num = int_num + diff_val
            larger_over_boundary = not (num_min <= temp_num <= num_max)
            if is_palindromic(str(int_num + diff_val)):
                return str(int_num + diff_val)

            diff_val += 1

        return ''


class TestSolution(object):
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
        ["num", "result"],
        [
            # ("222222222", "222222222"),
            ("123", "121"),
            ("1332", "1331"),
            ("12388", "12421"),
            ("12345", "12321"),
            ("1", "0"),
            ("13", "11"),
            ("1213", "1221"),
        ]
    )
    def test_nearestPalindromic(self, num, result):
        logging.info(f'testing: {num=}, {result=}')
        assert self.solution.nearestPalindromic(num) == result
        pass


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

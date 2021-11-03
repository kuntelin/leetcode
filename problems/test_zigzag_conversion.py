import argparse
import inspect
import logging
import re

import pytest

str_pattern = re.compile(r'^[a-z0-9,.]+$', re.I)


class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if not isinstance(s, str):
            raise ValueError

        if not 1 <= len(s) <= 1000:
            raise ValueError

        if str_pattern.match(s) is None:
            raise ValueError

        if not 1 <= numRows <= 1000:
            raise ValueError

        # corner case, data in one row or in one column
        if numRows == 1 or numRows > len(s):
            return s

        # prepare result temp array
        result_matrix = []
        [result_matrix.append([]) for i in range(numRows)]

        # get grouping number, each grouping have the same remainder
        if numRows <= 1:
            grouping = 1
        else:
            grouping = numRows + (numRows - 2)
        logging.debug(f'{grouping=}')

        for idx, char in enumerate(s):
            logging.debug(f'{idx=}, {char=}')

            # to separate the group and find the remainder
            """
            0   4   8     0   0   0
            1 3 5 7 9  => 1 3 1 3 1
            2   6         2   2
            """
            grouping_remainder = idx % grouping
            logging.debug(f'{grouping_remainder=}')

            # to find the row index to put the char
            """
            0   0   0    0   0   0
            1 3 1 3 1 => 1 1 1 1 1
            2   2        2   2
            """
            quotient, remainder = divmod(grouping_remainder, numRows - 1)
            logging.debug(f'{quotient=}, {remainder=}')
            if quotient == 0:
                row_idx = remainder
            else:
                row_idx = numRows - 1 - remainder
            logging.debug(f'{row_idx=}')

            result_matrix[row_idx].append(char)

        logging.debug(f'{result_matrix=}')

        result = ''.join(map(lambda x: ''.join(x), result_matrix))
        logging.debug(f'{result=}')

        return result


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if not isinstance(s, str):
            raise ValueError

        if not 1 <= len(s) <= 1000:
            raise ValueError

        if str_pattern.match(s) is None:
            raise ValueError

        if not 1 <= numRows <= 1000:
            raise ValueError

        # corner case, data in one row or in one column
        if numRows == 1 or numRows > len(s):
            return s

        # prepare result temp array
        result_matrix = []
        [result_matrix.append('') for i in range(numRows)]

        # get grouping number, each grouping have the same remainder
        if numRows <= 1:
            grouping = 1
        else:
            grouping = numRows + (numRows - 2)
        logging.debug(f'{grouping=}')

        for idx, char in enumerate(s):
            logging.debug(f'{idx=}, {char=}')

            # to separate the group and find the remainder
            """
            0   4   8     0   0   0
            1 3 5 7 9  => 1 3 1 3 1
            2   6         2   2
            """
            grouping_remainder = idx % grouping
            logging.debug(f'{grouping_remainder=}')

            # to find the row index to put the char
            """
            0   0   0    0   0   0
            1 3 1 3 1 => 1 1 1 1 1
            2   2        2   2
            """
            quotient, remainder = divmod(grouping_remainder, numRows - 1)
            logging.debug(f'{quotient=}, {remainder=}')
            if quotient == 0:
                row_idx = remainder
            else:
                row_idx = numRows - 1 - remainder
            logging.debug(f'{row_idx=}')

            result_matrix[row_idx] += char

        logging.debug(f'{result_matrix=}')

        result = ''.join(result_matrix)
        logging.debug(f'{result=}')

        return result


class TestSolution:
    def setup_class(self) -> None:
        # self.solution = Solution1()
        self.solution = Solution2()

    @pytest.mark.parametrize(
        ['input_str', 'input_row', 'answer'],
        [
            ({}, 1, ValueError),
            ([], 1, ValueError),
            (0, 1, ValueError),
            ('', 1, ValueError),
            ('a' * 1001, 1, ValueError),
            ('a', 0, ValueError),
            ('a', 1001, ValueError),
        ]
    )
    def test_valid_string(self, input_str, input_row, answer):
        with pytest.raises(answer):
            self.solution.convert(input_str, input_row)

    @pytest.mark.parametrize(
        ['input_str', 'input_row', 'answer'],
        [
            ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
            ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
            ('A', 1, 'A'),
        ]
    )
    def test_convert(self, input_str, input_row, answer):
        logging.debug(f'{inspect.currentframe().f_code.co_name}({input_str}, {input_row}, {answer})')

        result = self.solution.convert(input_str, input_row)
        assert result == answer


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

    pass


if __name__ == '__main__':
    main()

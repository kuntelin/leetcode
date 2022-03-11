import argparse
import logging
import pytest
import sys
# sys.path.append('.')
from problems import TimeMethodMixin


class Solution:
    def intToRoman(self, num: int) -> str:
        char_mapping = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }
        result = []
        for x in sorted(char_mapping.keys(), reverse=True):
            logging.debug(f'x is {x}')
            a, b = divmod(num, x)

            if a:
                result.append(char_mapping[x] * a)
                logging.debug(f'result is now {result}')

                num = num - x * a
                logging.debug(f'num is now {num}')

        return ''.join(result)


class TestSolution(TimeMethodMixin):
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["num", "result"],
        [
            (3, 'III'),
            (58, 'LVIII'),
            (1994, 'MCMXCIV'),
        ],
    )
    def test_answer(self, num, result):
        logging.debug('execute function')
        response = self.time_method(self.solution.intToRoman, *(num, ), **{})

        logging.debug('compare output')
        assert response == result

    def teardown_method(self, method):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-cli-level', action='store', type=str.upper, default='WARNING')

    # exclusive_group = parser.add_mutually_exclusive_group()
    # exclusive_group.add_argument('--verbose', action='store_true')
    # exclusive_group.add_argument('--debug', action='store_true')

    args = parser.parse_args()

    logging.getLogger().setLevel(logging.getLevelName(args.log_cli_level))

    logging.info('info message')
    logging.debug('debug message')


if __name__ == '__main__':
    main()

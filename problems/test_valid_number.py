import argparse
import logging

import pytest


class Solution:
    def isNumber(self, s: str) -> bool:
        _number = _exponent = _dot = False
        for idx, char in enumerate(s):
            if char.isdigit():
                _number = True
            elif char in ("+", "-"):
                if idx > 0 and s[idx - 1] != "e" and s[idx - 1] != "E":
                    return False
            elif char in ("e", "E"):
                if _exponent or not _number:
                    return False
                _exponent = True
                _number = False
            elif char == ".":
                if _dot or _exponent:
                    return False
                _dot = True
            else:
                return False

        return _number


class TestSolution:
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
            ("2", True),
            ("0089", True),
            ("-0.1", True),
            ("+3.14", True),
            ("4.", True),
            ("-.9", True),
            ("2e10", True),
            ("-90E3", True),
            ("3e+7", True),
            ("+6e-1", True),
            ("53.5e93", True),
            ("-123.456e789", True),
        ]
    )
    def test_valid(self, num, result):
        logging.info(f'testing: {num=}, {result=}')
        assert self.solution.isNumber(num) == result
        pass

    @pytest.mark.parametrize(
        ["num", "result"],
        [
            ("abc", False),
            ("1a", False),
            ("1e", False),
            ("e2", False),
            ("99e2.5", False),
            ("--6", False),
            ("-+3", False),
            ("95a54e53", False),
            ("6+1", False),
            (".", False),
            ("+.", False),
            (".+", False),
        ]
    )
    def test_invalid(self, num, result):
        logging.info(f'testing: {num=}, {result=}')
        assert self.solution.isNumber(num) == result
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

    pass


if __name__ == '__main__':
    main()

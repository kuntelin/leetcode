import argparse
import logging

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def isValid1(self, s: str) -> bool:
        close_mappping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        process_stack = []
        for symbol in s:
            close_symbol = close_mappping.get(symbol, None)

            # symbol is not a close symbol, add to prcoess stack
            if close_symbol is None:
                process_stack.append(symbol)
                continue

            # symbol is a close symbol, but not thing to close, return not valid
            if not process_stack:
                return False

            # symbol is not the same, return not valid
            if process_stack.pop() != close_symbol:
                return False

        return not process_stack

    def isValid2(self, s: str) -> bool:
        close_mapping = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        process_stack = []
        for c in s:
            if c in close_mapping:
                # it's a open symbol, add to process stack
                process_stack.append(c)
            else:
                # threat all as close symbol

                # nothing to close, return not valid
                if not process_stack:
                    return False

                # close symbol not matched, return not valid
                if close_mapping.get(process_stack.pop(), None) != c:
                    return False

        # return valid if process_stack is empty
        return not process_stack


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["s", "expected"],
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
        ],
    )
    def test_isValid1(self, s: str, expected: bool):
        assert self.solution.isValid1(s) == expected

    @pytest.mark.parametrize(
        ["s", "expected"],
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
        ],
    )
    def test_isValid2(self, s: str, expected: bool):
        assert self.solution.isValid2(s) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log-cli-level", action="store", type=str.upper, default="WARNING"
    )
    args = parser.parse_args()

    logging.getLogger().setLevel(logging.getLevelName(args.log_cli_level))


if __name__ == "__main__":
    main()

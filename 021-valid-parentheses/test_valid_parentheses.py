import logging

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        bracket_hash = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        close_chars = []
        for c in s:
            logger.debug(f"{c=}")

            # 括號開頭，將括號結束放入close_chars
            if c in bracket_hash:
                close_chars.insert(0, bracket_hash[c])
                continue

            # 檢查是否為對的括號結束
            if len(close_chars) != 0 and close_chars[0] == c:
                close_chars.pop(0)
                continue

            # 錯誤的括號結束，直接回傳False
            return False

        return len(close_chars) == 0


param_names = "s,expected"
param_values = [
    ("[]", True),
    ("([{}])", True),
    ("[(])", False),
    ("]", False),
    ("]]", False),
]


@pytest.mark.parametrize(param_names, param_values)
def test_valid_parentheses(benchmark, s: str, expected: bool):
    solution = Solution()
    result = benchmark(solution.isValid, s)
    assert result == expected

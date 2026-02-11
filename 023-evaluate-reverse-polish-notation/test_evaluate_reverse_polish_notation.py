import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for t in tokens:
            if t == "+":
                ans.append(ans.pop(-2) + ans.pop(-1))
            elif t == "-":
                ans.append(ans.pop(-2) - ans.pop(-1))
            elif t == "*":
                ans.append(ans.pop(-2) * ans.pop(-1))
            elif t == "/":
                ans.append(int(ans.pop(-2) / ans.pop(-1)))
            else:
                ans.append(int(t))

        return ans.pop(0)


param_names = "tokens,expected"
param_values = [
    (["1", "2", "+", "3", "*", "4", "-"], 5),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
]


@pytest.mark.parametrize(param_names, param_values)
def test_valid_parentheses(benchmark, tokens: List[str], expected: int):
    solution = Solution()
    result = benchmark(solution.evalRPN, tokens)

    assert result == expected

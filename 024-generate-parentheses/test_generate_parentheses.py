import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        利用s當迴圈的暫存器，當open_num close_num n都相等時，代表此為最後的結果，只需組成字串回傳就好
        再用遞回的方式找出可能的組合
        """

        s = []
        ans = []

        def generate_parenthesis(open_num: int, close_num: int):
            logger.debug(f"f{open_num=},{close_num=},{s=}")
            if open_num == close_num == n:
                ans.append("".join(s))
                return

            if open_num < n:
                s.append("(")
                generate_parenthesis(open_num + 1, close_num)
                s.pop()

            if close_num < open_num:
                s.append(")")
                generate_parenthesis(open_num, close_num + 1)
                s.pop()

        generate_parenthesis(0, 0)

        return ans


param_names = "n,expected"
param_values = [
    (1, ["()"]),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
]


@pytest.mark.parametrize(param_names, param_values)
def test_generate_parentheses(benchmark, n: int, expected: List[str]):
    solution = Solution()
    result = benchmark(solution.generateParenthesis, n)

    assert result == expected

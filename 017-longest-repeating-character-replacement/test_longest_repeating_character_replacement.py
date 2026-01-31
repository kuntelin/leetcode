import logging
from collections import defaultdict

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        假設符合規定的字串為target，
        則target為連續字串(l_idx:r_idx)內，最常出現的字數加上可替換的字數總合最大值
        而答案為所有target的最大值

        由於不知道target值，所以由左自右依序增加target長度，並在所有符合的條件中找出最大值
        """

        longest = 0
        l_idx, r_idx = 0, 0
        char_freq = defaultdict(int)

        # 依序增加長度(移動右邊界)直到上限
        for r_idx in range(len(s)):
            logger.debug(f"{l_idx=}, {r_idx=}")

            # 統計字數
            char_freq[s[r_idx]] += 1

            # 超過可替換的上限，縮短長度(移動左邊界)
            if (r_idx - l_idx + 1) - max(char_freq.values()) > k:
                char_freq[s[l_idx]] -= 1
                l_idx += 1

            logger.debug(f"{l_idx=}, {r_idx=}, {char_freq=}")

            # 重新比較最大長度
            longest = max(longest, r_idx - l_idx + 1)

        return longest


param_names = "s,k,expected"
param_values = [
    ("XYYX", 2, 4),
    ("AAABABB", 1, 5),
]


@pytest.mark.parametrize(param_names, param_values)
def test_longest_repeating_character_replacement(benchmark, s: str, k: int, expected: int):
    solution = Solution()

    result = benchmark(solution.characterReplacement, s, k)
    assert result == expected

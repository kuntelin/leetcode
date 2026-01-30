import logging

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for idx in range(len(s)):
            unique_chars = set()
            for loop in range(idx, len(s)):
                if s[loop] in unique_chars:
                    break

                unique_chars.add(s[loop])

            # calculate the longest value
            longest = max(longest, len(unique_chars))

        return longest

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        運用二個定位點，進行長度的比較，而不需要再多跑一次迴圈
        固定增加右邊定位點，並檢查有無重覆字元
            有重覆字元： 代表新的子字串出現，移除最左方的字元直到調整成為新的子字串
            無重覆字元： 將目前的字元加入，重新計算及比較最大長度
        """
        longest = 0
        unique_chars = set()
        l_idx, r_idx = 0, 0
        for r_idx in range(len(s)):
            logger.debug(f"{l_idx=}, {r_idx=}, {unique_chars=}")

            # 字元已有出現，一直移除直至沒重覆為止，同時將左邊定位增加
            while s[r_idx] in unique_chars:
                unique_chars.remove(s[l_idx])
                l_idx += 1

            # 將目前字元加入
            unique_chars.add(s[r_idx])

            # 重新計算及比較最大長度
            longest = max(longest, r_idx - l_idx + 1)

        return longest


param_names = "s,expected"
param_values = [
    ("zxyzxyz", 3),
    ("xxxx", 1),
    (" ", 1),
    ("au", 2),
]


@pytest.mark.parametrize(param_names, param_values)
def test_longest_substring_without_repeating_characters1(benchmark, s: str, expected: int):
    solution = Solution()

    result = benchmark(solution.lengthOfLongestSubstring, s)
    assert result == expected


@pytest.mark.parametrize(param_names, param_values)
def test_longest_substring_without_repeating_characters2(benchmark, s: str, expected: int):
    solution = Solution()

    result = benchmark(solution.lengthOfLongestSubstring2, s)
    assert result == expected

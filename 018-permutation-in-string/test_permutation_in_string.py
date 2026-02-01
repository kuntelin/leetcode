import logging

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        因為s1必需在s2內，所以可用s1的長度查找s2內，是否有長度一樣且字元出現頻率一樣的子字串，
        要注意的是如果dict內，數量為0的key必需要用del刪除，否則會讓比較結果不一致
        """
        if len(s1) > len(s2):
            return False

        window_size = len(s1)
        l_idx, r_idx = 0, 0
        s1_freq = {}
        char_freq = {}

        # 計算s1的字元及其出現的頻率
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        logger.debug(f"{s1_freq=}")

        for r_idx in range(len(s2)):
            char_freq[s2[r_idx]] = char_freq.get(s2[r_idx], 0) + 1

            # 是否超出s1的長度，超過則位移左邊界
            if r_idx - l_idx + 1 > window_size:
                char_freq[s2[l_idx]] -= 1

                # ! 頻率為零，直接移除該key
                if char_freq[s2[l_idx]] == 0:
                    del char_freq[s2[l_idx]]

                l_idx += 1

            logger.debug(f"{l_idx=}, {r_idx=}, {char_freq=}")

            # 已符結果但不在此判斷，直接離開迴圈以減少相同判斷式
            if s1_freq == char_freq:
                break

        logger.debug(f"{s1_freq=}, {char_freq=}")

        # 統一由此回傳結果，以避免改A忘B的狀況
        return s1_freq == char_freq


param_names = "s1,s2,expected"
param_values = [
    ("abc", "lecabee", True),
    ("abc", "lecaabee", False),
]


@pytest.mark.parametrize(param_names, param_values)
def test_permutation_in_string(benchmark, s1: str, s2: str, expected: bool):
    solution = Solution()

    result = benchmark(solution.checkInclusion, s1, s2)
    assert result == expected

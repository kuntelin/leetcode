import logging
from collections import defaultdict

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        在S中找出符合T的最短字串，是在所有可能的字串中，找出含有T目標內的字元且數量要一致，
        由左向右找出符合條件的字串，接著再試著將其縮短，再比較所有符合的字串中最短的
        要注意在計算滿足需求條件時，用數量相等做開關，但只能計算一次
        """
        # T是空的，回傳空字串
        if t == "":
            return ""

        # S的長度小於T的長度，不會有符合的結果，回傳空字串
        if len(s) < len(t):
            return ""

        # 目標字串中，字元及出現頻率的對照
        required_hash = defaultdict(int)
        for c in t:
            required_hash[c] += 1
        # 目標字串中，需要滿足字元及頻率的個數
        required_count = len(required_hash.keys())

        # 目前字串中，字元及出現頻率的對照
        compared_hash = defaultdict(int)
        # 目前字串中，已滿足字元與頻率相符的個數
        fulfilled_counter = 0

        # 符合的最短字串長度，設定為原始字串+1，
        minium_length = len(s) + 1

        logger.info("進行字串比對任務")
        answer, l_idx, r_idx = "", 0, 0
        for r_idx in range(len(s)):
            compared_hash[s[r_idx]] += 1

            # 計算字元及出現頻率是否與要求的相符
            logger.info("計算字元及出現頻率是否滿足需求...")
            if s[r_idx] in required_hash and compared_hash[s[r_idx]] == required_hash[s[r_idx]]:
                logger.info(f"字元 {s[r_idx]} 完成需求條件!")
                logger.debug(f"{s[r_idx]=}, {compared_hash[s[r_idx]]=}, {required_hash[s[r_idx]]=}")
                fulfilled_counter += 1

            # 未滿足比對條件，繼續增長字串
            logger.info("計算完成的需求數量是否達標...")
            if fulfilled_counter != required_count:
                logger.info("未達標，繼續計算!")
                logger.debug(f"{fulfilled_counter=}, {required_count=}")
                continue

            # 滿足比對條件，嘗試縮短字串
            logger.info("已達標，嘗試縮短字串")
            while fulfilled_counter == required_count:
                # 與目前最短字串做比較
                if r_idx - l_idx + 1 < minium_length:
                    logger.info("找到新的最短字串，更新最短字串!")
                    logger.debug(f"{l_idx=}, {r_idx}, {s[l_idx:r_idx+1]=}")
                    minium_length = r_idx - l_idx + 1
                    answer = s[l_idx : r_idx + 1]

                # 移除左邊界的字元並重新計算其出現頻率
                compared_hash[s[l_idx]] -= 1
                if s[l_idx] in required_hash and compared_hash[s[l_idx]] < required_hash[s[l_idx]]:
                    fulfilled_counter -= 1

                # 位移左邊界
                l_idx += 1

        return answer if minium_length != len(s) + 1 else ""


param_names = "s,t,expected"
param_values = [
    ("OUZODYXAZV", "XYZ", "YXAZ"),
    ("xyz", "xyz", "xyz"),
    ("x", "xy", ""),
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("aaaaaaaaaaaabbbbbcdd", "abcdd", "abbbbbcdd"),
]


@pytest.mark.parametrize(param_names, param_values)
def test_permutation_in_string(benchmark, s: str, t: str, expected: str):
    solution = Solution()

    result = benchmark(solution.minWindow, s, t)
    assert result == expected

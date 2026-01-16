import pytest
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        result_dict = {}
        for s in strs:
            hash_key = "".join(sorted(s))

            if hash_key not in result_dict.keys():
                result_dict[hash_key] = []

            result_dict[hash_key].append(s)

        return list(result_dict.values())

    def anagrams(self, str1, str2) -> bool:
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # * using defaultdict for better code and performance

        if len(strs) == 1:
            return [strs]

        result_dict = defaultdict(list)
        for s in strs:
            result_dict["".join(sorted(s))].append(s)

        return list(result_dict.values())

@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["act", "pots", "tops", "cat", "stop", "hat"],
            [
                ["act", "cat"],
                ["pots", "tops", "stop"],
                ["hat"],
            ],
        ),
        (["x"], [["x"]]),
        ([""], [[""]])
    ],
)
def test_group_anagram(strs: List[str], expected: List[List[str]]):
    solution = Solution()
    assert solution.groupAnagrams(strs) == expected

import logging
import unittest


class Solution:
    @staticmethod
    def get_substr(substr):
        chars = []
        for char in substr:
            if char not in chars:
                chars.append(char)
            else:
                break
        return chars

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not (0 <= len(s) <= 5 * (10 ** 4)):
            raise ValueError

        substr_list = []
        for idx in range(len(s)):
            substr_list.append(self.get_substr(s[idx:]))
        logging.error(substr_list)
        if not substr_list:
            max_len = 0
        else:
            max_len = max(map(lambda item: len(item), substr_list))

        return max_len

        # substr = []
        # substr_list = []
        # for current_char in s:
        #     if current_char not in substr:
        #         substr.append(current_char)
        #     else:
        #         substr_list.append(substr)
        #         substr = [current_char]
        # substr_list.append(substr)
        # print(substr_list)
        # max_len = max(map(lambda item: len(item), substr_list))

        # return max_len


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self):
        assert self.solution.lengthOfLongestSubstring('abcabcbb') == 3
        assert self.solution.lengthOfLongestSubstring('bbbbb') == 1
        assert self.solution.lengthOfLongestSubstring('pwwkew') == 3
        assert self.solution.lengthOfLongestSubstring(' ') == 1
        assert self.solution.lengthOfLongestSubstring('dvdf') == 3

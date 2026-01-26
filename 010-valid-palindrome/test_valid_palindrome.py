import logging
import re

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove not allowed chars
        cleaned_s = re.sub(r"[^a-zA-Z0-9]", "", s)
        cleaned_length = len(cleaned_s)
        logger.debug(f"{cleaned_s=}, {cleaned_length=}")

        idx = 0
        while idx < (cleaned_length - idx):
            rev_idx = cleaned_length - idx - 1

            logger.debug(f"{idx=}, {rev_idx=}, {cleaned_s[idx].lower()=}, {cleaned_s[rev_idx].lower()=}")

            # char not the same
            if cleaned_s[idx].lower() != cleaned_s[rev_idx].lower():
                return False

            idx += 1

        return True


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Was it a car or a cat I saw?", True),
        ("tab a cat", False),
    ],
)
def test_valid_palindrome(s: str, expected: bool):
    solution = Solution()
    assert solution.isPalindrome(s) == expected

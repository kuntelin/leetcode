import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("xx", "x", False),
        ("bbcc", "ccbc", False),
    ],
)
def test_valid_anagram(s: str, t: str, expected: bool):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected

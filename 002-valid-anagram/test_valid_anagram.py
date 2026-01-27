import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


param_names = "s, t, expected"
param_values = (
    ("racecar", "carrace", True),
    ("jar", "jam", False),
    ("xx", "x", False),
    ("bbcc", "ccbc", False),
)


@pytest.mark.parametrize(param_names, param_values)
def test_valid_anagram(benchmark, s: str, t: str, expected: bool):
    solution = Solution()

    result = benchmark(solution.isAnagram, s, t)
    assert result == expected

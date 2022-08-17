import logging
import pytest
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:  # noqa
        nums1 = self.nums
        nums2 = vec.nums

        if len(nums1) != len(nums2):
            raise ValueError

        if not 1 <= len(nums1) <= 10 ** 5:
            raise ValueError

        if any(map(lambda x: not 0 <= x <= 100, nums1)) or any(map(lambda x: not 0 <= x <= 100, nums2)):
            raise ValueError

        result = 0
        for num1, num2 in zip(nums1, nums2):
            result += num1 * num2

        return result


class TestSparseVector:
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["v1", "v2", "result"],
        [
            ([1, 0, 0, 2, 3], [0, 3, 0, 4, 0], 8),
            ([0, 1, 0, 0, 0], [0, 0, 0, 0, 2], 0),
            ([0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4], 6),
        ]
    )
    def test_numRescueBoats(self, v1: List[int], v2: List[int], result: int):  # noqa
        v1 = SparseVector(v1)
        v2 = SparseVector(v2)
        assert v1.dotProduct(v2) == result

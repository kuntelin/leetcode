import pytest
import logging
from typing import List

logger = logging.getLogger(__name__)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    result[x] *= nums[y]
        logger.debug(f"{result=}")
        return result

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        product_all, zero_counter = 1, 0
        for n in nums:
            if n == 0:
                zero_counter += 1
            else:
                product_all *= n

        if zero_counter > 1:
            # * if the zero value more then one time, then all the value will be zero
            return [0] * len(nums)
        elif zero_counter == 1:
            # * if there is one zero value, the all other value is zero expect that one
            result = []
            for idx, num in enumerate(nums):
                result.append(0 if nums[idx] else product_all)
        else:
            # * there is not zero, return the product_all divided by current number
            result = [product_all // num for num in nums]

        logger.debug(f"{result=}")

        return result


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 4, 6], [48, 24, 12, 8]),
        ([-1, 0, 1, 2, 3], [0, -6, 0, 0, 0]),
    ],
)
def test_product_of_array_expect_self(nums: List[int], expected: List[int]):
    solution = Solution()
    assert solution.productExceptSelf2(nums) == expected
    assert 1 == 1

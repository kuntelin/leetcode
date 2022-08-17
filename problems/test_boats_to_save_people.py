import logging
import pytest
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:  # noqa
        if not people:
            return 0

        if not 1 <= len(people) <= 5 * (10 ** 4):
            raise ValueError

        if not 1 <= limit <= 3 * (10 ** 4):
            raise ValueError

        if any(map(lambda x: not 1 <= x <= limit, people)):
            raise ValueError

        people.sort()

        boats = 0
        left_pointer = 0
        right_pointer = len(people) - 1
        while left_pointer <= right_pointer:
            # fat person can carry one thin person, remove one thin person
            if people[left_pointer] + people[right_pointer] <= limit:
                left_pointer += 1

            # fat person with one boat
            boats += 1
            right_pointer -= 1

        return boats


class TestSolution:
    def setup_class(self):
        self.solution = Solution()

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["people", "limit", "result"],
        [
            ([1, 2], 3, 1),
            ([3, 2, 2, 1], 3, 3),
            ([3, 5, 3, 4], 5, 4),
            ([2, 4], 5, 2),
        ]
    )
    def test_numRescueBoats(self, people: List[int], limit: int, result: int):  # noqa
        logging.info(f'{people=}, {limit=}, {result=}')
        assert self.solution.numRescueBoats(people, limit) == result

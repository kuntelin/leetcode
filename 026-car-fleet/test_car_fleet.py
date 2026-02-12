import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0 and 1 car
        if len(position) < 2:
            return len(position)

        # combine car position and speed into set, sort by position in descending order
        car_info = sorted(zip(position, speed), reverse=True)
        logger.debug(f"{car_info=}")

        car_fleet = []
        for pos, spd in car_info:
            # 計算到target需要幾次並記錄到stack
            car_fleet.append((target - pos) / spd)

            # 判斷第一台之後的車輛，如果到目標的次數少於前車(會超車)，則合併車隊
            if len(car_fleet) >= 2 and car_fleet[-1] <= car_fleet[-2]:
                car_fleet.pop()

        logger.debug(f"{car_fleet=}")

        return len(car_fleet)


param_names = "target,position,speed,expected"
param_values = [
    (10, [1, 4], [3, 2], 1),
    (10, [4, 1, 0, 7], [2, 2, 1, 1], 3),
    (20, [15, 4, 10, 12, 17, 19, 11, 14, 6, 0, 2], [4, 8, 1, 2, 8, 8, 10, 7, 10, 8, 6], 5),
    (100, [0, 2, 4], [4, 2, 1], 1),
]


@pytest.mark.parametrize(param_names, param_values)
def test_car_fleet(benchmark, target: int, position: List[int], speed: List[int], expected: int):
    solution = Solution()
    result = benchmark(solution.carFleet, target, position, speed)
    assert result == expected

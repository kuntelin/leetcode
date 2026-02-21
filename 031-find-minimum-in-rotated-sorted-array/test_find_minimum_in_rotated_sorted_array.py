import logging

import pytest

logger = logging.getLogger(__name__)


param_names = ""
param_values = [
    (),
]


@pytest.mark.parametrize(param_names, param_values)
def test_find_minimum_in_rotated_sorted_array(benchmark):
    raise NotImplementedError

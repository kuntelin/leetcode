import logging

import pytest

logger = logging.getLogger(__name__)

param_names = ""
param_values = [
    (),
]


@pytest.mark.parametrize(param_names, param_values)
def test_copy_test_with_random_pointer(benchmark):
    raise NotImplementedError

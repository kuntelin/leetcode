import logging

import pytest

logger = logging.getLogger(__name__)

param_names = ""
param_values = [
    (),
]


@pytest.mark.parametrize(param_names, param_values)
def test_koko_eating_bananas(benchmark):
    raise NotImplementedError

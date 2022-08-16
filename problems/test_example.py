import argparse
import logging

import pytest

from problems.utils import echo


class Solution:
    @staticmethod
    def echo(arg):
        return echo(arg)


class TestSolution:
    def setup_class(self):
        self.solution = Solution()
        pass

    def teardown_class(self):
        pass

    def setup_method(self, method):
        pass

    @pytest.mark.parametrize(
        ["echo_input", "echo_back"],
        [
            (1, 1),
            ("a", "a"),
            ([], []),
        ],
    )
    @pytest.mark.benchmark
    def test_echo(self, echo_input, echo_back):
        logging.info(f'{echo_input=}, {echo_back=}')
        assert self.solution.echo(echo_input) == echo_back

    def teardown_method(self, method):
        pass


def main():
    parser = argparse.ArgumentParser()
    exclusive_group = parser.add_mutually_exclusive_group()
    exclusive_group.add_argument('--verbose', action='store_true')
    exclusive_group.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)
    elif args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    solution = Solution()
    assert solution.echo(1) == 1
    assert solution.echo("a") == "a"
    assert solution.echo([]) == []


if __name__ == '__main__':
    main()

import logging
from typing import List

import pytest

logger = logging.getLogger(__name__)


class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f";{len(s)}#{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0
        get_length_flag = False
        get_length_str = ""
        while idx < len(s):
            logger.debug(f"{idx=},{s[idx]=}")
            try:
                if s[idx] == ";":
                    # start of new string
                    get_length_flag = True
                    get_length_str = ""
                    idx += 1

                elif get_length_flag and s[idx] != "#":
                    # append the string length
                    get_length_str += s[idx]
                    idx += 1

                elif get_length_flag and s[idx] == "#":
                    # get the string
                    idx += 1  # move to the begin of string
                    result.append(str(s[idx : idx + int(get_length_str)]))
                    idx += int(get_length_str)  # move to the end of string

                    # reset get_length
                    get_length_flag = False
                    get_length_str = ""
                else:
                    logger.error("unknown situation...")
            except IndexError:
                logger.error("out of idex error!!")
                break

        logger.debug(f"{result=}")

        return result


@pytest.mark.parametrize(
    "dummy_input",
    [["Hello", "World"], [""]],
)
def test_encode_and_decode_strings(dummy_input: List[str]):
    solution = Solution()
    assert dummy_input == solution.decode(solution.encode(dummy_input))

import argparse
import inspect
import logging
import re

import pytest

str_pattern = re.compile(r'^[0-9a-z]+$', re.I)


def is_valid_string(input_string: str) -> bool:
    logging.debug(f'{inspect.currentframe().f_code.co_name}({input_string})')

    return str_pattern.match(input_string) is not None


def is_palindromic_string(input_string: str) -> bool:
    logging.debug(f'{inspect.currentframe().f_code.co_name}({input_string})')

    input_length = len(input_string)

    # check string length less than 3
    if input_length == 0:
        return False
    elif input_length == 1:
        return True
    elif input_length == 2:
        return input_string[0] == input_string[1]
    else:
        pass

    quotient, remainder = divmod(input_length, 2)
    logging.debug(f'{quotient=}, {remainder=}')
    for idx in range(quotient):
        f_idx = idx
        b_idx = (quotient * 2 - idx) - (input_length - remainder + 1)

        logging.debug(f'{f_idx=} {input_string[f_idx]=}, {b_idx=} {input_string[b_idx]=}')
        if not input_string[f_idx] == input_string[b_idx]:
            return False

    return True


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # check is string
        if not isinstance(s, str):
            raise ValueError

        # check string length
        if not (1 <= len(s) <= 1000):
            raise ValueError

        # check string content
        if not is_valid_string(s):
            raise ValueError

        return self.find_longest_palindrome_3(s)

    @staticmethod
    def find_longest_palindrome_1(s: str) -> int:
        """
        using for loop, poor performance
        """
        s_len = len(s)
        palindromic_list = []
        for start_idx, char in enumerate(s):
            for finish_idx in range(start_idx, s_len + 1):
                logging.debug(f'{s_len=}, {start_idx=}, {finish_idx=}, {s[start_idx:finish_idx]=}')

                substr = s[start_idx:finish_idx]
                if is_palindromic_string(substr):
                    palindromic_list.append(substr)

        return len(set(palindromic_list))

    @staticmethod
    def find_longest_palindrome_2(s: str) -> str:
        """
        using for loop, poor performance
        """
        logging.debug(f'{inspect.currentframe().f_code.co_name}')

        s_len = len(s)
        palindromic_max = ''
        palindromic_len = 0
        for start_idx, char in enumerate(s):
            finish_idx = s.rfind(char, start_idx, s_len)

            while finish_idx >= 0:
                logging.debug(f'{char=}, {start_idx=}, {finish_idx=}, {s[start_idx:finish_idx + 1]}')
                substr = s[start_idx:finish_idx + 1]

                # the sub string is shorter than palindromic max string, by pass it
                if (finish_idx - start_idx + 1) < palindromic_len:
                    break

                if start_idx == finish_idx and palindromic_max == '':
                    palindromic_max = substr
                    palindromic_len = len(substr)
                    break

                # the sub string is palindromic string and is longer than palindromic max string,
                # set the palindromic max string to this sub string
                if is_palindromic_string(substr):
                    if len(substr) > len(palindromic_max):
                        palindromic_max = substr
                        palindromic_len = len(substr)
                        break

                # finding the next possible palindromic string
                finish_idx = s.rfind(char, start_idx, finish_idx)

        return palindromic_max

    @staticmethod
    def find_longest_palindrome_3(s: str) -> str:
        def get_max_palindrome_len(substr: str, left: int, right: int) -> int:
            logging.debug(f'{inspect.currentframe().f_code.co_name}, {left=}, {right=}')

            substr_len = len(substr)
            while left >= 0 and right < substr_len and s[left] == s[right]:
                logging.debug(f'checking {left=}, {right=}, {s[left]=}, {s[right]=}')
                left -= 1
                right += 1

            return right - left - 1

        start = end = 0
        for i in range(len(s)):
            # get odd palindrome string length
            odd_palindrome_len = get_max_palindrome_len(s, i, i)

            # get even palindrome string length
            even_palindrome_len = get_max_palindrome_len(s, i, i + 1)

            max_len = max(odd_palindrome_len, even_palindrome_len)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end + 1]


class TestSolution(object):
    def setup_class(self) -> None:
        self.solution = Solution()

    @pytest.mark.parametrize(
        ['input_string', 'answer'],
        [
            ('', False),
            ('a', True),
            ('0', True),
            ('a0', True),
            ('0a', True),
            ('+', False),
            ('+a', False),
            ('a+', False),
            ('+0', False),
            ('0+', False),
            ('aaa', True),
            ('000', True),
            ('a+0', False),
            ('0+a', False),
        ]
    )
    @pytest.mark.benchmark
    def test_is_valid_string(self, benchmark, input_string, answer):
        result = benchmark(is_valid_string, input_string)
        assert result == answer

    @pytest.mark.parametrize(
        ['input_data'],
        [
            (1, ),
            ([], ),
            ({}, ),
            (object(), ),
        ]
    )
    def test_is_not_string(self, input_data):
        with pytest.raises(ValueError):
            self.solution.longestPalindrome(input_data)

    @pytest.mark.parametrize(
        ['input_data'],
        [
            ('',),
            ('a' * 1001,),
        ]
    )
    def test_string_length_is_invalid(self, benchmark, input_data):
        with pytest.raises(ValueError):
            benchmark(self.solution.longestPalindrome, input_data)

    @pytest.mark.parametrize(
        ['input_data', 'answer'],
        [
            ('', False),
            ('a', True),
            ('0', True),
            ('a0', False),
            ('0a', False),
            ('aa', True),
            ('00', True),
            ('aba', True),
            ('bab', True),
            ('abc', False),
            ('cab', False),
            ('a0a', True),
            ('0a0', True),
            ('abba', True),
            ('abccba', True),
            ('abc00cba', True),
        ]
    )
    @pytest.mark.benchmark
    def test_is_palindromic_string(self, benchmark, input_data, answer):
        result = benchmark(is_palindromic_string, input_data)
        assert result == answer

    @pytest.mark.parametrize(
        ['input_data', 'answer'],
        [
            ('babad', 'aba'),
            ('cbbd', 'bb'),
            ('a', 'a'),
            ('ac', 'c'),
            ('aaabaaaa', 'aaabaaa'),
            # (),
            # (),
        ]
    )
    @pytest.mark.benchmark
    def test_longestPalindrome(self, benchmark, input_data, answer):
        result = benchmark(self.solution.longestPalindrome, input_data)
        assert result == answer


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

    # solution = Solution()
    # logging.info(solution.longestPalindrome('babad'))
    # logging.info(solution.longestPalindrome('cbbd'))
    # logging.info(solution.longestPalindrome('a'))
    # logging.info(solution.longestPalindrome('ac'))
    # logging.info(solution.longestPalindrome('aaabaaaa'))
    # logging.info(solution.longestPalindrome('anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg'))
    # logging.info(solution.longestPalindrome('reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye'))
    pass


if __name__ == '__main__':
    main()

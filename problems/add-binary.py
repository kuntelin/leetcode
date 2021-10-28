class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not (1 <= len(a) <= 10 ** 4):
            raise ValueError

        if not (1 <= len(b) <= 10 ** 4):
            raise ValueError

        for _char in a:
            if _char != '0' and _char != '1':
                raise ValueError

        for _char in b:
            if _char != '0' and _char != '1':
                raise ValueError

        max_len = max(len(a), len(b))
        plus_bit = 0
        result = []
        for idx in range(1, max_len + 1):
            try:
                a_bit = a[-idx]
            except IndexError:
                a_bit = 0

            try:
                b_bit = b[-idx]
            except IndexError:
                b_bit = 0

            all_bit = int(a_bit) + int(b_bit) + plus_bit

            if all_bit == 0:
                result.append(0)
                plus_bit = 0
            elif all_bit == 1:
                result.append(1)
                plus_bit = 0
            elif all_bit == 2:
                result.append(0)
                plus_bit = 1
            elif all_bit == 3:
                result.append(1)
                plus_bit = 1
            else:
                raise ValueError

            print(f'a_bit: {a_bit}, b_bit: {b_bit}, plus_bit: {plus_bit}')

        if plus_bit == 1:
            result.append(1)

        return ''.join([str(i) for i in result[::-1]])


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('11', '1'))
    print(solution.addBinary('1010', '1011'))
    print(solution.addBinary(
        "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
        "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011",
    ))

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        plus_idx1 = num1.index('+')
        real1 = int(num1[:plus_idx1])
        imag1 = int(num1[plus_idx1+1:-1])

        plus_idx2 = num2.index('+')
        real2 = int(num2[:plus_idx2])
        imag2 = int(num2[plus_idx2+1:-1])

        real_part = real1 * real2 - imag1 * imag2
        imag_part = real1 * imag2 + real2 * imag1
        return f'{real_part}+{imag_part}i'

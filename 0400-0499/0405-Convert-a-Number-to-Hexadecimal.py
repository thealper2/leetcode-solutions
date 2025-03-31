class Solution:
    def toHex(self, num: int) -> str:
        hex_digits = "0123456789abcdef"
        result = ""

        if num == 0:
            return "0"

        if num < 0:
            num += 1 << 32

        while num >= 1:
            result = hex_digits[num % 16] + result
            num //= 16

        return result

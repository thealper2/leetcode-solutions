class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        i = 1
        while num >= 1:
            k = 1 - num % 2
            result += i * k
            num = num // 2
            i *= 2

        return result
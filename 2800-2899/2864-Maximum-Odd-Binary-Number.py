class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = s.count('1')
        count_0 = len(s) - count_1
        return '1' * (count_1 - 1) + '0' * count_0 + '1'
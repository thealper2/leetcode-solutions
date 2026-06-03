class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        str_n = str(n)
        digits = set(str_n)
        result = 0
        for digit in digits:
            result += str_n.count(digit) * int(digit)

        return result
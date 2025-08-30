from collections import defaultdict


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        digits = defaultdict(int)
        temp = n

        while temp > 0:
            digits[temp % 10] += 1
            temp //= 10

        min_freq = min(digits.values())
        return min(digit for digit, freq in digits.items() if freq == min_freq)

class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        for digit in set(n):
            max_digit = max(int(digit), max_digit)

        return max_digit

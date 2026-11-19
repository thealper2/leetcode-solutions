class Solution:
    def minRotations(self, s: str) -> int:
        prev = 0
        result = 0
        for d in s:
            digit = int(d)
            result += min(abs(digit - prev), 10 - abs(digit - prev))
            prev = digit

        return result
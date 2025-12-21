class Solution:
    def mirrorDistance(self, n: int) -> int:
        digits = []
        i = 0

        while 10**i <= n:
            d = n // 10**i % 10
            digits.append(d)
            i += 1
        
        result = 0
        for p in range(i):
            result += digits[i - p - 1] * (10 ** p)

        return abs(result - n)

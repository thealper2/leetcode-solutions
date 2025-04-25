import math


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_s = a ** 2 + b ** 2
                c = int(math.isqrt(c_s))

                if c * c == c_s and 1 <= c <= n:
                    count += 1

        return count
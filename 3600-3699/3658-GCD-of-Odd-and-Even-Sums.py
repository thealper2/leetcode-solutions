import math


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odds = 0
        evens = 0
        for i in range(1, n * 2 + 1):
            if i % 2 == 0:
                evens += i
            else:
                odds += i

        return math.gcd(odds, evens)

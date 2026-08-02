import math

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        nums_sorted = sorted(nums, reverse=True)
        best = 0

        n = len(nums_sorted)
        limit = min(n, 100)

        for i in range(limit):
            for j in range(i + 1, limit):
                a = nums_sorted[i]
                b = nums_sorted[j]
                g = math.gcd(a, b)
                strength = (a * b) // (g * g)
                if strength > best:
                    best = strength

        if best == 0:
            for i in range(n):
                for j in range(i + 1, n):
                    a = nums_sorted[i]
                    b = nums_sorted[j]
                    g = math.gcd(a, b)
                    strength = (a * b) // (g * g)
                    if strength > best:
                        best = strength
        
        return best

class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        result = 0

        if m <= k and n <= k:
            return 0

        if m > k and n <= k:
            result += (m - k) * k

        if n > k and m <= k:
            result += (n - k) * k

        return result

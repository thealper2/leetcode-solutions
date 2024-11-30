class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        f = 0
        while f < n:
            f = i + (f + 2)
            i += 1

        return i
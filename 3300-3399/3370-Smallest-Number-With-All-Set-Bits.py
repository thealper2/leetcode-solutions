class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 1
        while True:
            x = (2 ** k) - 1
            if x >= n:
                return x
            k += 1
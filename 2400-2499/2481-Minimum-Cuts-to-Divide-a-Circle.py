class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n % 2 == 1 and n > 1:
            return n

        return n // 2
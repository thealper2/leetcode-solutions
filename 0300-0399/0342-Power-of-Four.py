class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        while n > 4:
            n /= 4

        return n == 4

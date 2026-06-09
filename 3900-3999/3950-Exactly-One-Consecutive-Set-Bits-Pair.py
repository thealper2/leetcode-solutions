class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        cnt = 0
        while n > 0:
            if n & 3 == 3:
                cnt += 1

            n >>= 1

        return cnt == 1

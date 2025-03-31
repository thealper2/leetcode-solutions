class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start >= 1 or goal >= 1:
            b1 = start % 2
            b2 = goal % 2

            if b1 != b2:
                count += 1

            start //= 2
            goal //= 2

        return count
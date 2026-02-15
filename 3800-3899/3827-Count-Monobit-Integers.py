class Solution:
    def countMonobit(self, n: int) -> int:
        if n < 0:
            return 0

        count = 1
        k = 1
        while (1 << k) - 1 <= n:
            count += 1
            k += 1

        return count

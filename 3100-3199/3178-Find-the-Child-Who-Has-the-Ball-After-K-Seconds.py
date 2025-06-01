class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        reverse = 1
        idx = 0
        for _ in range(k):
            idx += reverse
            if idx == 0 or idx == n - 1:
                reverse *= -1

        return idx
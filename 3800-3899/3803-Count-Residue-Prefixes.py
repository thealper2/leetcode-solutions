class Solution:
    def residuePrefixes(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(1, n + 1):
            prefix = s[:i]
            if len(set(prefix)) == len(prefix) % 3:
                cnt += 1

        return cnt

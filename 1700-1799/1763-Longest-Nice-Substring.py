class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_len = 0
        max_nice = ""
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]

                if set(sub) == set(sub.swapcase()):
                    if len(sub) > max_len:
                        max_len = len(sub)
                        max_nice = sub

        return max_nice

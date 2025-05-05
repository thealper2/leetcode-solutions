class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        n = len(s)

        count = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                count += 1
                if count > max_len:
                    max_len = count
            else:
                count = 1

        return max_len
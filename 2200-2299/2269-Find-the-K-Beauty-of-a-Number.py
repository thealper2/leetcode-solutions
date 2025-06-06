class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        count = 0

        for i in range(0, n - k + 1):
            sub = s[i:i+k]
            if int(sub) > 0 and num % int(sub) == 0:
                count += 1

        return count
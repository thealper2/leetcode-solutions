class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverse_s = s[::-1]
        n = len(s)
        for i in range(n - 1):
            subset = reverse_s[i:i + 2]
            if subset in s:
                return True

        return False
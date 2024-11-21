class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if (s[i] != " ") and (i == 0 or s[i - 1] == " "):
                result += 1

        return result
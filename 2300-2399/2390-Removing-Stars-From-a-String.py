class Solution:
    def removeStars(self, s: str) -> str:
        result = ""

        for c in s:
            if c == '*':
                result = result[:-1]
            else:
                result += c

        return result
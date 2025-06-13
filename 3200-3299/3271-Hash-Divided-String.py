class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        n = len(s)

        for i in range(0, n, k):
            sub = s[i:i+k]
            total = 0
            for c in sub:
                total += ord(c) - ord('a')

            result += chr((total % 26) + ord('a'))

        return result

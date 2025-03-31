class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        count = 0

        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == t[j]:
                    count += abs(i - j)

        return count
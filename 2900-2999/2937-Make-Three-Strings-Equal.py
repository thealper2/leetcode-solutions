class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        i = 0
        max_substr = 0
        while i < min(l1, l2, l3):
            if s1[i] == s2[i] == s3[i]:
                max_substr += 1
            else:
                break

            i += 1

        if max_substr > 0:
            return l1 + l2 + l3 - 3 * max_substr

        return -1

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        count_ones = s.count('1')
        count_zeros = 0
        result = 0

        for i in range(n - 1):
            if s[i] == '1':
                count_ones -= 1
            else:
                count_zeros += 1

            result = max(result, count_zeros + count_ones)

        return result

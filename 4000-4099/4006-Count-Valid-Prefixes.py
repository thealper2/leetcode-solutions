class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count = 0
        zeros = 0
        ones = 0

        for i, c in enumerate(s):
            if c == '0':
                zeros += 1
            else:
                ones += 1

            if abs(ones - zeros) <= 1:
                count += 1

        return count

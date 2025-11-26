class Solution:
    def minOperations(self, s: str) -> int:
        total = 0
        for c in s:
            if c != 'a':
                total = max(total, (ord('a') - ord(c)) % 26)

        return total

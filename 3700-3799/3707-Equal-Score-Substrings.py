class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        scores = [ord(c) - ord('a') + 1 for c in s]
        for i in range(n):
            if sum(scores[:i]) == sum(scores[i:]):
                return True

        return False

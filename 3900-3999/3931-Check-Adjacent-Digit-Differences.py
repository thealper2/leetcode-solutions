class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n = len(s)
        for i in range(n - 1):
            a, b = map(int, list(s[i:i+2]))
            if abs(a - b) > 2:
                return False 

        return True
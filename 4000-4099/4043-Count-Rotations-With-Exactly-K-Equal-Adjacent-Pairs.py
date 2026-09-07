class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        
        if k < 0 or k > n - 1:
            return 0
        
        equal = [0] * n
        total_equal = 0
        for i in range(n):
            if s[i] == s[(i + 1) % n]:
                equal[i] = 1
                total_equal += 1
        
        count = 0
        for i in range(n):
            removed_idx = (i + n - 1) % n
            score = total_equal - equal[removed_idx]
            if score == k:
                count += 1
        
        return count

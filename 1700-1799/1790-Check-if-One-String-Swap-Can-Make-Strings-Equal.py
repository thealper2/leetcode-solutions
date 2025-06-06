class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 != l2:
            return False
        
        diff = []
        for i in range(l1):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
        
        if not diff:
            return True
            
        if len(diff) != 2:
            return False
        
        i, j = diff
        return s1[i] == s2[j] and s1[j] == s2[i]
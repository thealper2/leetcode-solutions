class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        idx = 0
            
        while idx <= len(s) - n:
            if s[idx:idx+n] == part:
                s = s[:idx] + s[idx+n:]
                idx = 0
                continue
            
            idx += 1
                
        return s

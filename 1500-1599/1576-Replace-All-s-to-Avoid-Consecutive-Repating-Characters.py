class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        
        for i in range(n):
            if s[i] == '?':
                left = s[i-1] if i > 0 else 'A'
                right = s[i+1] if i < n-1 else 'A'
                
                for c in range(97, 123):
                    if c != ord(left) and c != ord(right):
                        s[i] = chr(c)
                        break
                        
        return ''.join(s)

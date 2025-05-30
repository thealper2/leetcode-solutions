class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                t1 = s[:l] + s[l + 1:]
                t2 = s[:r] + s[r + 1:]
                return t1 == t1[::-1] or t2 == t2[::-1]
            
            l += 1
            r -= 1
        
        return True

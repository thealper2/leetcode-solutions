class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        
        while l < r:
            if s[l] > s[r]:
                s[l] = s[r]
            elif s[l] < s[r]:
                s[r] = s[l]

            l += 1
            r -= 1

        return ''.join(s)
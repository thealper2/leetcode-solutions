class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0
        vowels = "aeiouAEIOU"

        while l < r:
            if s[l] in vowels:
                count += 1
            
            if s[r] in vowels:
                count -= 1

            l += 1
            r -= 1

        return count == 0
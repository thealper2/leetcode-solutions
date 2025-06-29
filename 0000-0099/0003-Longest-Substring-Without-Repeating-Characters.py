class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        i = 0
        max_sub = 1

        while i < n - max_sub:
            sub = s[i:i+max_sub+1]
            if len(set(sub)) == len(sub):
                max_sub += 1
            else:
                i += 1

        return max_sub
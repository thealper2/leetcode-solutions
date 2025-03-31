class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += (27 - (ord(s[i].lower()) - 96)) * (i + 1) 
        
        return result
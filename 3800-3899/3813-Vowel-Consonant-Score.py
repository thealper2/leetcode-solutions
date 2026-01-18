class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set('aeiou')
        v = 0
        c = 0
        
        for char in s:
            if char.isalpha():
                if char in vowels:
                    v += 1
                else:
                    c += 1
        
        if c == 0:
            return 0
        
        return v // c

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = set()
        uppercase = set()
        for c in word:
            if c.islower():
                lowercase.add(c)
            else:
                uppercase.add(c.lower())
        
        special = 0
        for c in lowercase:
            if c in uppercase:
                special += 1
        
        return special
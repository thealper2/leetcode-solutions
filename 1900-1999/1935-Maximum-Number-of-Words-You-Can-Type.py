class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = set(brokenLetters)
        n = len(words)
        
        for word in words:
            for c in word:
                if c in broken:
                    n -= 1
                    break

        return n
class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        
        for c in text:
            if c == ' ':
                spaces += 1

        words = [word.strip() for word in text.split()]
        
        if len(words) == 1:
            return words[0] + ' ' * spaces

        n = spaces // (len(words) - 1)

        extra = spaces % (len(words) - 1)

        result = (' ' * n).join(words)
        result += ' ' * extra
        return result

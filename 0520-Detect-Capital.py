class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[1:] == word[1:].lower() or word == word.upper():
            return True
        else:
            return False
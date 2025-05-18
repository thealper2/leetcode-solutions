import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = r'^[a-z]*([a-z]-[a-z])?[a-z]*[!,.]?$|^[!,.]$'
        tokens = sentence.split()
        count = 0
        for token in tokens:
            if re.fullmatch(pattern, token):
                count += 1
        return count
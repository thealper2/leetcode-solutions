from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(words)
        result = ''

        for i in range(n):
            result += words[i]
            if result == s:
                return True
            
        return False
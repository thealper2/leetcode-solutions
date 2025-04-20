from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)
            good = True
            for char, count in word_count.items():
                if chars_count[char] < count:
                    good = False
                    break
        
            if good:
                total += len(word)

        return total
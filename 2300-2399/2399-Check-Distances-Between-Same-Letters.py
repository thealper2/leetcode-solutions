from typing import List
from collections import defaultdict


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        letters = defaultdict(list)
        
        for index, char in enumerate(s):
            letters[char].append(index)
        
        for char in letters:
            f, s = letters[char]
            actual = s - f - 1 
            expected = distance[ord(char) - ord('a')]
            if actual != expected:
                return False
        
        return True
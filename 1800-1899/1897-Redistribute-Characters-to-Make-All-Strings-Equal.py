from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        count = defaultdict(int)

        for word in words:
            for c in word:
                count[c] += 1
            
        for k, v in count.items():
            if v < n or v % n != 0:
                return False

        return True
        
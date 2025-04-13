from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c = 0
        for w in words:
            if s.startswith(w):
                c += 1
        return c
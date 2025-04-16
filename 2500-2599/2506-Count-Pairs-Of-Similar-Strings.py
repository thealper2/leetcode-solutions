from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        c = 0
        for i in range(n):
            for j in range(i + 1, n):
                if set(words[i]) == set(words[j]):
                    c += 1

        return c
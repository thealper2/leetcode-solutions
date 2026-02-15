from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        for word in words:
            weight = 0
            for c in word:
                weight += weights[ord(c) - ord('a')]

            result += chr(ord('a') + 26 - (weight % 26) - 1)

        return result

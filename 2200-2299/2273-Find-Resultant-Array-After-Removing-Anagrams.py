from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        result = []

        for i in range(n):
            if i == 0 or sorted(words[i]) != sorted(words[i - 1]):
                result.append(words[i])

        return result
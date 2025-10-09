from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = set(words)
        result = ''
        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in words:
                    valid = False
                    break

            if valid:
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word

        return result

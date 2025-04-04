from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (words[i] == words[j][::-1]):
                    count += 1

        return count
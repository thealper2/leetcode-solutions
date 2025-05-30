from collections import defaultdict


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        frequencies = sorted(count.values())
        deletions = 0
        distinct = len(frequencies)

        while distinct > k:
            deletions += frequencies.pop(0)
            distinct -= 1

        return deletions

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for c in arr:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        return len(set(d.values())) == len(d.values())
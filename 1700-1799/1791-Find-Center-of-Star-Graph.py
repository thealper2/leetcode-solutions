from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}
        for edge in edges:
            for c in edge:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1

        return max(d, key=d.get)
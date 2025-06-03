from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        count = 0
        n = len(g)
        
        for cookie in s:
            if cookie >= g[count]:
                count += 1
                if count == n:
                    break

        return count
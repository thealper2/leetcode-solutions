from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        h = len(s)
        l = 0
        result = []

        for c in s:
            if c == "I":
                result.append(l)
                l += 1
            else:
                result.append(h)
                h -= 1

        result.append(l)
        return result
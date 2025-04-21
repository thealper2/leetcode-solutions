from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        curr = 0
        total = 1

        for c in s:
            idx = ord(c) - ord('a')
            w = widths[idx]

            if curr + w > 100:
                total += 1
                curr = w

            else:
                curr += w

        return [total, curr]
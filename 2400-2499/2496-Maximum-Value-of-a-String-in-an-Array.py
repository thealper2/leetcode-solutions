from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m = 0
        for s in strs:
            is_numeric = True
            for char in s:
                if not (char >= '0' and char <= '9'):
                    is_numeric = False
                    break

            if is_numeric and s:
                curr = int(s)
            else:
                curr = len(s)

            if curr > m:
                m = curr

        return m
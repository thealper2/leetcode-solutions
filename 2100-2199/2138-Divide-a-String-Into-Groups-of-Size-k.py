from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        result = []
        for i in range(0, n, k):
            result.append(s[i:i+k].ljust(k, fill))

        return result

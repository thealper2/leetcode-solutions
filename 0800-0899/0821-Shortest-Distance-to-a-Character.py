from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [float('-inf')] * n
        last_c = float('-inf')

        for i in range(n):
            if s[i] == c:
                last_c = i

            result[i] = i - last_c

        last_c = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_c = i

            result[i] = min(result[i], last_c - i)

        return result
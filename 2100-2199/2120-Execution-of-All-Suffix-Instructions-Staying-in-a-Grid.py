from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        result = [0] * m
        for i in range(m):
            r, c = startPos
            cnt = 0
            for j in range(i, m):
                if s[j] == 'L':
                    c -= 1
                elif s[j] == 'R':
                    c += 1
                elif s[j] == 'U':
                    r -= 1
                elif s[j] == 'D':
                    r += 1

                if r < 0 or r >= n or c < 0 or c >= n:
                    break

                cnt += 1

            result[i] = cnt

        return result

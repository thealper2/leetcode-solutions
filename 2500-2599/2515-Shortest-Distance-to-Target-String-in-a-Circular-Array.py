from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        
        n = len(words)
        found = False

        for i in range(n):
            if words[(startIndex + i) % n] == target:
                found = True
                break

        if not found:
            return -1

        for j in range(n):
            if words[(startIndex - j) % n] == target:
                break

        return min(i, j)
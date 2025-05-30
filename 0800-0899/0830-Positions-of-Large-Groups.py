from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = end = 0
        n = len(s)
        result = []

        for end in range(n):
            if end == n - 1 or s[end] != s[end + 1]:
                if end - start + 1 >= 3:
                    result.append([start, end])
                
                start = end + 1
                
        return result

        return result

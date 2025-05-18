from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]
        
        if end < start:
            most = list(range(1, end + 1)) + list(range(start, n + 1))
        else:
            most = list(range(start, end + 1))
            
        return most
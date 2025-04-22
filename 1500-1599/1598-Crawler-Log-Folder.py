from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n = 0
        for log in logs:
            if log == "../":
                if n:
                    n -= 1
            elif log != "./":
                n += 1
        
        return n